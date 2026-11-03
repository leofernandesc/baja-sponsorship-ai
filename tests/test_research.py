from pathlib import Path
from copy import deepcopy

import pytest
from pydantic import ValidationError

from baja_sponsorship.research.fixtures import JsonFixtureProvider
from baja_sponsorship.research.models import ResearchReport
from baja_sponsorship.research.service import ResearchService, outgoing_approved_facts

FIXTURE = Path(__file__).parent / "fixtures" / "synthetic_resolved.json"


def base_data():
    return ResearchReport.model_validate_json(FIXTURE.read_text()).model_dump(mode="json")


def test_fixture_is_valid_but_claim_not_approved():
    report = ResearchService(JsonFixtureProvider(FIXTURE)).run(" Example  Engineering ")
    assert report.identity.canonical_name.endswith("(fictional)")
    assert outgoing_approved_facts(report) == []


def test_wrong_company_input_is_rejected():
    with pytest.raises(ValueError, match="different input"):
        ResearchService(JsonFixtureProvider(FIXTURE)).run("Different Corporation")


def test_missing_citation_is_rejected():
    data = base_data()
    data["claims"][0]["evidence_source_ids"] = []
    with pytest.raises(ValidationError, match="linked to a source"):
        ResearchReport.model_validate(data)


def test_unknown_source_id_is_rejected():
    data = base_data()
    data["claims"][0]["evidence_source_ids"] = ["invented"]
    with pytest.raises(ValidationError, match="unknown source"):
        ResearchReport.model_validate(data)


def test_duplicate_evidence_ids_are_rejected():
    data = base_data()
    data["sources"].append(deepcopy(data["sources"][0]))
    with pytest.raises(ValidationError, match="unique"):
        ResearchReport.model_validate(data)


def test_unreviewed_claim_cannot_be_approved_by_ai():
    data = base_data()
    data["claims"][0]["review_status"] = "approved"
    with pytest.raises(ValidationError, match="operational management"):
        ResearchReport.model_validate(data)


def test_management_review_allows_approved_claim():
    data = base_data()
    data["claims"][0]["review_status"] = "approved"
    data["claims"][0]["reviewer_role"] = "operational_management"
    report = ResearchReport.model_validate(data)
    assert len(outgoing_approved_facts(report)) == 1


def test_ambiguous_company_must_not_assert_facts():
    data = base_data()
    data["identity"] = {
        "input_name": "Example Engineering",
        "status": "ambiguous",
        "canonical_name": None,
        "official_website": None,
        "identity_source_ids": [],
        "candidates": ["Example One", "Example Two"],
    }
    with pytest.raises(ValidationError, match="before resolving"):
        ResearchReport.model_validate(data)


def test_ambiguous_company_without_facts_is_valid():
    data = base_data()
    data["identity"] = {
        "input_name": "Example Engineering",
        "status": "ambiguous",
        "canonical_name": None,
        "official_website": None,
        "identity_source_ids": [],
        "candidates": ["Example One", "Example Two"],
    }
    data["claims"] = []
    report = ResearchReport.model_validate(data)
    assert outgoing_approved_facts(report) == []


def test_unknown_identity_reference_is_rejected():
    data = base_data()
    data["identity"]["identity_source_ids"] = ["made_up"]
    with pytest.raises(ValidationError, match="unknown evidence source"):
        ResearchReport.model_validate(data)


def test_naive_source_timestamp_is_rejected():
    data = base_data()
    data["sources"][0]["retrieved_at"] = "2026-11-03T12:00:00"
    with pytest.raises(ValidationError, match="timezone"):
        ResearchReport.model_validate(data)


def test_empty_company_input_is_rejected():
    with pytest.raises(ValueError, match="between 1 and 200"):
        ResearchService(JsonFixtureProvider(FIXTURE)).run("   ")
