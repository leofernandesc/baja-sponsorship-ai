"""Recorded-source replay: actual public Bosch/SAE URLs verified on 2026-11-03.

This test does NOT call the OpenAI API. It verifies the adapter's response-shape
and safety boundaries using claims grounded manually in public sources.
"""
from types import SimpleNamespace as Obj
from baja_sponsorship.research.openai_provider import (
    ExtractedClaim, ExtractionResult, OpenAIWebResearchProvider,
)
from baja_sponsorship.research.models import ClaimType, IdentityStatus, ReviewStatus, SourceType
from baja_sponsorship.research.service import ResearchService, outgoing_approved_facts

BOSCH_CONTACT = 'https://www.bosch.com.br/contato/'
BOSCH_BUSINESS = 'https://www.bosch.com.br/nossa-empresa/grupo-bosch-no-mundo/'
SAE_EVENT = 'https://legado.saebrasil.org.br/competicao-baja-sae-brasil-etapa-nacional-2026-tem-62-equipes-inscritas/'

class FakeResponses:
    def __init__(self, extraction):
        self.extraction = extraction
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(('web_search', kwargs))
        sources = [Obj(url=url, title=title) for url, title in (
            (BOSCH_CONTACT, 'Contato | Bosch no Brasil'),
            (BOSCH_BUSINESS, 'Grupo Bosch no mundo'),
            (SAE_EVENT, 'Baja SAE Brasil etapa nacional 2026')
        )]
        return Obj(
            output=[Obj(type='web_search_call', action=Obj(sources=sources))],
            output_text='Bosch has a corporate sponsorship form. Mobility includes sensors. SAE lists Bosch as national Baja sponsor in 2026.',
        )

    def parse(self, **kwargs):
        self.calls.append(('extract', kwargs))
        return Obj(output_parsed=self.extraction)


def extraction(claims):
    return ExtractionResult(
        identity_status=IdentityStatus.RESOLVED,
        canonical_name='Grupo Bosch (operação brasileira)',
        official_website=BOSCH_CONTACT,
        identity_supporting_urls=[BOSCH_CONTACT],
        candidates=[], claims=claims, unknowns=[], limitations=[],
    )


def test_real_source_replay_research_builds_linked_drafts():
    claims = [
        ExtractedClaim(text='A Bosch aceita pedidos de patrocínio corporativo sem incentivo por formulário e indica prazo de análise de três meses.', claim_type=ClaimType.FACT, supporting_urls=[BOSCH_CONTACT]),
        ExtractedClaim(text='A Bosch atua em sistemas de sensores, unidades de controle, semicondutores e powertrain.', claim_type=ClaimType.FACT, supporting_urls=[BOSCH_BUSINESS]),
        ExtractedClaim(text='A Bosch patrocinou a competição nacional Baja SAE Brasil de 2026.', claim_type=ClaimType.FACT, supporting_urls=[SAE_EVENT]),
    ]
    client=Obj(responses=FakeResponses(extraction(claims)))
    report=ResearchService(OpenAIWebResearchProvider(client,'mock-model')).run('Bosch')
    assert report.identity.status is IdentityStatus.RESOLVED
    assert len(report.sources)==3
    assert len(report.claims)==3
    assert all(c.review_status is ReviewStatus.SOURCE_LINKED for c in report.claims)
    assert all(c.evidence_source_ids for c in report.claims)
    assert not outgoing_approved_facts(report)
    assert client.responses.calls[0][1]['store'] is False
    assert client.responses.calls[1][1]['store'] is False


def test_real_source_replay_rejects_unobserved_url():
    claims=[ExtractedClaim(text='Empresa fornecerá gratuitamente componentes.',claim_type=ClaimType.FACT,supporting_urls=['https://unknown.example/fake'])]
    report=OpenAIWebResearchProvider(Obj(responses=FakeResponses(extraction(claims))),'mock-model').research('Bosch')
    assert report.claims==[]
    assert any('Discarded claim' in s for s in report.limitations)


def test_valid_url_does_not_guarantee_claim_truth():
    # Claim is false/unsupported by linked source, but existing adapter only checks URL provenance.
    claims=[ExtractedClaim(text='A Bosch já patrocina diretamente a equipe BAJA UEA.',claim_type=ClaimType.FACT,supporting_urls=[SAE_EVENT])]
    report=OpenAIWebResearchProvider(Obj(responses=FakeResponses(extraction(claims))),'mock-model').research('Bosch')
    assert len(report.claims)==1  # Semantics NOT checked by E2 provider, expected limitation.
    assert report.claims[0].review_status is ReviewStatus.SOURCE_LINKED
    assert outgoing_approved_facts(report)==[]  # Cannot reach approved outbound facts.


def test_source_type_not_classified_yet():
    report=OpenAIWebResearchProvider(Obj(responses=FakeResponses(extraction([]))),'mock-model').research('Bosch')
    assert all(source.source_type is SourceType.OTHER for source in report.sources)
