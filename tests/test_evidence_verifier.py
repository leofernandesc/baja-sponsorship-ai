"""Offline adversarial evidence checks; no OpenAI key or network required."""
from datetime import datetime, timezone
from types import SimpleNamespace as Obj

from baja_sponsorship.research.evidence_verifier import (
    EvidenceVerifier, SourceReview, VerificationVerdict, excerpt_is_in_source,
)
from baja_sponsorship.research.models import (
    ResearchReport, CompanyIdentity, EvidenceSource, ResearchClaim,
    IdentityStatus, ClaimType, ReviewStatus, SourceType,
)
from baja_sponsorship.research.openai_judge import OpenAISourceJudge
from baja_sponsorship.research.service import outgoing_approved_facts

URL_A = 'https://www.bosch.com.br/contato/'
URL_B = 'https://legado.saebrasil.org.br/competicao-baja-sae-brasil-etapa-nacional-2026-tem-62-equipes-inscritas/'
TEXT_A = 'Os projetos incentivados ou não são analisados e respondidos dentro de um prazo de três meses. A proposta será avaliada.'
TEXT_B = 'A Bosch é patrocinadora da Competição Baja SAE Brasil Etapa Nacional 2026. O evento ocorre em março de 2026.'
NOW = datetime.now(timezone.utc)


def report(text='A Bosch analisa pedidos de patrocínio em três meses.', extra_source=False):
    sources = [EvidenceSource(source_id='s1',url=URL_A,title='Bosch',source_type=SourceType.COMPANY_OFFICIAL,retrieved_at=NOW)]
    if extra_source:
        sources.append(EvidenceSource(source_id='s2',url=URL_B,title='SAE',source_type=SourceType.SAE_OR_UNIVERSITY,retrieved_at=NOW))
    return ResearchReport(
        researched_at=NOW,
        identity=CompanyIdentity(input_name='Bosch',canonical_name='Bosch Brasil', status=IdentityStatus.RESOLVED,identity_source_ids=['s1']),
        sources=sources, claims=[ResearchClaim(claim_id='c1',text=text,claim_type=ClaimType.FACT,
                                                evidence_source_ids=['s1','s2'] if extra_source else ['s1'],review_status=ReviewStatus.SOURCE_LINKED)],
    )


class Fetcher:
    def __init__(self, texts):self.texts=texts;self.calls=[]
    def fetch(self,url):
        self.calls.append(url)
        if url not in self.texts:raise ValueError('missing fixture')
        return self.texts[url]


class Judge:
    def __init__(self, answers):self.answers=answers;self.calls=[]
    def judge(self, *,claim,source_text,source_url):
        self.calls.append((claim,source_url))
        return self.answers[source_url]


def test_verified_quote_supported_but_not_approved():
    judge=Judge({URL_A:SourceReview(verdict='supported',verbatim_excerpt='analisados e respondidos dentro de um prazo de três meses.',rationale='Explicit review window')})
    result=EvidenceVerifier(Fetcher({URL_A:TEXT_A}),judge).verify(report())
    assert result.checks[0].verdict is VerificationVerdict.SUPPORTED
    assert result.checks[0].requires_human_approval
    assert not outgoing_approved_facts(report())
    assert result.checks[0].source_sha256['s1']


def test_hallucinated_quote_cannot_pass_even_when_judge_says_supported():
    judge=Judge({URL_A:SourceReview(verdict='supported',verbatim_excerpt='A Bosch confirmou que financiará o BAJA UEA em 2027.',rationale='Guess')})
    check=EvidenceVerifier(Fetcher({URL_A:TEXT_A}),judge).verify(report()).checks[0]
    assert check.verdict is VerificationVerdict.INSUFFICIENT
    assert not check.excerpts


def test_weak_short_quote_fails():
    assert not excerpt_is_in_source('A Bosch',TEXT_A)
    judge=Judge({URL_A:SourceReview(verdict='supported',verbatim_excerpt='Os projetos',rationale='Too short')})
    assert EvidenceVerifier(Fetcher({URL_A:TEXT_A}),judge).verify(report()).checks[0].verdict is VerificationVerdict.INSUFFICIENT


def test_misleading_valid_url_judge_catches_false_direct_team_sponsorship():
    judge=Judge({URL_B:SourceReview(verdict='insufficient',verbatim_excerpt='',rationale='Only event sponsorship')})
    r=report('Bosch patrocina diretamente a equipe BAJA UEA.')
    r.sources=[EvidenceSource(source_id='s1',url=URL_B,title='SAE',source_type=SourceType.SAE_OR_UNIVERSITY,retrieved_at=NOW)]
    checked=EvidenceVerifier(Fetcher({URL_B:TEXT_B}),judge).verify(r)
    assert checked.checks[0].verdict is VerificationVerdict.INSUFFICIENT


def test_conflicting_sources_prevent_supported_result():
    judge=Judge({
        URL_A:SourceReview(verdict='supported',verbatim_excerpt='analisados e respondidos dentro de um prazo de três meses.'),
        URL_B:SourceReview(verdict='contradicted',verbatim_excerpt='A Bosch é patrocinadora da Competição Baja SAE Brasil Etapa Nacional 2026.')
    })
    checked=EvidenceVerifier(Fetcher({URL_A:TEXT_A,URL_B:TEXT_B}),judge).verify(report(extra_source=True))
    assert checked.checks[0].verdict is VerificationVerdict.CONFLICTING


def test_unavailable_sources_fail_closed_and_judge_not_called():
    judge=Judge({})
    checked=EvidenceVerifier(Fetcher({}),judge).verify(report())
    assert checked.checks[0].verdict is VerificationVerdict.SOURCE_UNAVAILABLE
    assert judge.calls==[]


def test_unresolved_identity_never_invokes_verifier():
    r=ResearchReport(researched_at=NOW,identity=CompanyIdentity(input_name='Bosch', status=IdentityStatus.UNRESOLVED))
    checker=EvidenceVerifier(Fetcher({}),Judge({}))
    assert checker.verify(r).checks==[]


def test_max_claims_is_bounded_and_report_partial():
    r=report();r.claims.append(ResearchClaim(claim_id='c2',text='Outro fato',claim_type=ClaimType.FACT,evidence_source_ids=['s1']))
    ans=SourceReview(verdict='supported',verbatim_excerpt='analisados e respondidos dentro de um prazo de três meses.')
    f=Fetcher({URL_A:TEXT_A}); checked=EvidenceVerifier(f,Judge({URL_A:ans}),max_claims=1).verify(r)
    assert len(checked.checks)==1 and checked.partial


def test_source_is_fetched_once_for_multiple_claims():
    r=report();r.claims.append(ResearchClaim(claim_id='c2',text='Outro fato',claim_type=ClaimType.FACT,evidence_source_ids=['s1']))
    ans=SourceReview(verdict='insufficient')
    f=Fetcher({URL_A:TEXT_A}); EvidenceVerifier(f,Judge({URL_A:ans})).verify(r)
    assert f.calls==[URL_A]


def test_openai_judge_sends_fetched_text_without_search_tool():
    class FakeResponses:
        def __init__(self):self.kw=None
        def parse(self,**kwargs):
            self.kw=kwargs
            return Obj(output_parsed=SourceReview(verdict='insufficient',rationale='no support'))
    fake=FakeResponses()
    verdict=OpenAISourceJudge(Obj(responses=fake),'test-model').judge(claim='Some claim',source_text=TEXT_A,source_url=URL_A)
    assert verdict.verdict is VerificationVerdict.INSUFFICIENT
    assert fake.kw['store'] is False
    assert not fake.kw.get('tools')
    assert TEXT_A in fake.kw['input'][1]['content']


def test_recorded_short_excerpt_from_live_bosch_page_is_literal_anchor():
    """One short public Bosch quote was independently read on 2026-11-03.

    This is a *snapshot replay*, not a new network request. The mock judge only
    exercises excerpt verification; it does not prove actual model entailment.
    """
    from pathlib import Path
    snippet=(Path(__file__).parent/'fixtures/bosch_official_short_excerpt.txt').read_text().strip()
    judge=Judge({URL_A: SourceReview(verdict='supported',verbatim_excerpt=snippet)})
    check=EvidenceVerifier(Fetcher({URL_A:snippet}),judge).verify(report()).checks[0]
    assert check.verdict is VerificationVerdict.SUPPORTED
    assert check.excerpts['s1']==snippet
