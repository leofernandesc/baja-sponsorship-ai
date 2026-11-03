from types import SimpleNamespace as Obj

import pytest

from baja_sponsorship.research.openai_provider import (
    ExtractedClaim, ExtractionResult, OpenAIWebResearchProvider,
    ResearchProviderError, clean_url, observed_sources,
)
from baja_sponsorship.research.models import IdentityStatus, ClaimType
from baja_sponsorship.research.service import ResearchService, outgoing_approved_facts


class FakeResponses:
    def __init__(self, search_output, extracted):
        self.search_output = search_output
        self.extracted = extracted
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(("search", kwargs))
        return self.search_output

    def parse(self, **kwargs):
        self.calls.append(("extract", kwargs))
        return Obj(output_parsed=self.extracted)


def search_payload(with_search=True, with_sources=True):
    output = []
    if with_search:
        sources = [Obj(url="https://example.org/about", title="About Example")] if with_sources else []
        output.append(Obj(type="web_search_call", action=Obj(sources=sources)))
    output.append(Obj(type="message", content=[Obj(annotations=[
        Obj(type="url_citation", url="https://example.org/activities", title="Example activities")
    ])]))
    return Obj(output=output, output_text="Fictional example company makes illustrative modules.")


def extracted(status="resolved", source="https://example.org/activities"):
    return ExtractionResult(
        identity_status=status,
        canonical_name="Example Eng (fictional)" if status=="resolved" else None,
        official_website="https://example.org/about" if status=="resolved" else None,
        identity_supporting_urls=["https://example.org/about"],
        candidates=["Example A", "Example B"] if status=="ambiguous" else [],
        claims=[ExtractedClaim(text="Synthetic claim about an invented company",claim_type="fact",supporting_urls=[source])],
        unknowns=[],limitations=[],
    )


def test_observed_sources_are_from_tool_or_annotations_only():
    data=observed_sources(search_payload())
    assert "https://example.org/about" in data
    assert "https://example.org/activities" in data


def test_live_adapter_mock_emits_only_source_linked_drafts():
    client=Obj(responses=FakeResponses(search_payload(),extracted()))
    report=ResearchService(OpenAIWebResearchProvider(client,"test-model")).run("Example Engineering")
    assert report.identity.status is IdentityStatus.RESOLVED
    assert len(report.claims)==1
    assert report.claims[0].evidence_source_ids
    assert outgoing_approved_facts(report)==[]
    assert client.responses.calls[0][1]["tool_choice"]=="required"
    assert client.responses.calls[0][1]["store"] is False


def test_model_invented_url_is_dropped():
    client=Obj(responses=FakeResponses(search_payload(),extracted(source="https://bad-site.invalid/story")))
    report=OpenAIWebResearchProvider(client,"test-model").research("Example Engineering")
    assert len(report.claims)==0
    assert any("Discarded claim" in x for x in report.limitations)


def test_search_must_actually_execute():
    client=Obj(responses=FakeResponses(search_payload(with_search=False),extracted()))
    with pytest.raises(ResearchProviderError,match="did not execute"):
        OpenAIWebResearchProvider(client,"test-model").research("Example Engineering")


def test_search_without_observed_urls_is_unresolved():
    payload=Obj(output=[Obj(type="web_search_call", action=Obj(sources=[]))],output_text="text")
    client=Obj(responses=FakeResponses(payload,extracted()))
    report=OpenAIWebResearchProvider(client,"test-model").research("Example Engineering")
    assert report.identity.status is IdentityStatus.UNRESOLVED
    assert report.claims==[]
    assert len(client.responses.calls)==1


def test_ambiguous_company_requires_resolution():
    client=Obj(responses=FakeResponses(search_payload(),extracted(status="ambiguous")))
    report=OpenAIWebResearchProvider(client,"test-model").research("Example Engineering")
    assert report.identity.status is IdentityStatus.AMBIGUOUS
    assert len(report.identity.candidates)==2
    assert report.claims==[]


def test_invented_identity_source_yields_unresolved():
    x=extracted()
    x.identity_supporting_urls=["https://other-site.invalid/not-real"]
    client=Obj(responses=FakeResponses(search_payload(),x))
    report=OpenAIWebResearchProvider(client,"test-model").research("Example Engineering")
    assert report.identity.status is IdentityStatus.UNRESOLVED


def test_refuse_url_credentials_and_nonhttp():
    assert clean_url("https://user:secret@example.org/about") is None
    assert clean_url("javascript:alert(1)") is None
