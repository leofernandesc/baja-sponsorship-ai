"""Fail-closed independent source-content checks for E2 research claims.

A source URL, or a quote that happens to appear in a page, does NOT authorize a
claim for publication. This module checks excerpt provenance and returns a
reviewable verdict; operational management still owns final approval.
"""
from __future__ import annotations

import hashlib
import re
from datetime import datetime, timezone
from enum import Enum
from typing import Protocol

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, model_validator

from .models import ClaimType, ResearchReport


class VerificationVerdict(str, Enum):
    SUPPORTED = "supported"
    CONTRADICTED = "contradicted"
    INSUFFICIENT = "insufficient"
    SOURCE_UNAVAILABLE = "source_unavailable"
    CONFLICTING = "conflicting"


class SourceContent(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source_id: str
    url: HttpUrl
    text: str = Field(min_length=1, max_length=100_000)
    retrieved_at: datetime

    @model_validator(mode="after")
    def aware_time(self):
        if self.retrieved_at.tzinfo is None:
            raise ValueError("source content timestamp must include a timezone")
        return self

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.text.encode("utf-8")).hexdigest()


class SourceReview(BaseModel):
    """LLM output: a reasoned decision and a verbatim, source-local excerpt."""
    model_config = ConfigDict(extra="forbid")
    verdict: VerificationVerdict
    verbatim_excerpt: str = ""
    rationale: str = ""


class ClaimVerification(BaseModel):
    model_config = ConfigDict(extra="forbid")
    claim_id: str
    verdict: VerificationVerdict
    source_ids_checked: list[str] = Field(default_factory=list)
    source_sha256: dict[str, str] = Field(default_factory=dict)
    excerpts: dict[str, str] = Field(default_factory=dict)
    notes: list[str] = Field(default_factory=list)
    requires_human_approval: bool = True


class VerificationReport(BaseModel):
    model_config = ConfigDict(extra="forbid")
    researched_company: str
    verified_at: datetime
    checks: list[ClaimVerification]
    partial: bool = False


class DocumentFetcher(Protocol):
    def fetch(self, url: str) -> str: ...


class SourceJudge(Protocol):
    def judge(self, *, claim: str, source_text: str, source_url: str) -> SourceReview: ...


def whitespace_normalize(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def excerpt_is_in_source(excerpt: str, text: str) -> bool:
    """Strict literal anchoring, allowing only whitespace variation."""
    normalized = whitespace_normalize(excerpt)
    return len(normalized) >= 25 and normalized in whitespace_normalize(text)


class EvidenceVerifier:
    def __init__(self, fetcher: DocumentFetcher, judge: SourceJudge, *,
                 max_claims: int = 6, max_sources_per_claim: int = 2,
                 max_source_chars: int = 15000):
        if not (1 <= max_claims <= 30 and 1 <= max_sources_per_claim <= 5
                and 100 <= max_source_chars <= 50000):
            raise ValueError("invalid evidence verification limits")
        self.fetcher = fetcher
        self.judge = judge
        self.max_claims = max_claims
        self.max_sources_per_claim = max_sources_per_claim
        self.max_source_chars = max_source_chars

    def verify(self, report: ResearchReport) -> VerificationReport:
        # Avoid network/LLM calls when identity is ambiguous or unresolved.
        if report.identity.status.value != "resolved":
            return VerificationReport(
                researched_company=report.identity.input_name,
                verified_at=datetime.now(timezone.utc), checks=[], partial=bool(report.claims))
        sources = {s.source_id: s for s in report.sources}
        cache: dict[str, tuple[str | None, str]] = {}
        checks: list[ClaimVerification] = []
        facts = [c for c in report.claims if c.claim_type is ClaimType.FACT]
        for claim in facts[:self.max_claims]:
            per_source: list[VerificationVerdict] = []
            checked: list[str] = []
            excerpts: dict[str, str] = {}
            hashes: dict[str, str] = {}
            notes: list[str] = []
            for sid in list(dict.fromkeys(claim.evidence_source_ids))[:self.max_sources_per_claim]:
                src = sources[sid]  # ResearchReport validates all foreign keys.
                checked.append(sid)
                url = str(src.url)
                if sid not in cache:
                    try:
                        whole = self.fetcher.fetch(url)
                        if not whole.strip():
                            raise ValueError("empty source text")
                        cache[sid] = (whole[:self.max_source_chars], "")
                    except Exception as exc:  # fail closed: never use unverified content
                        cache[sid] = (None, type(exc).__name__)
                text, failure = cache[sid]
                if text is None:
                    per_source.append(VerificationVerdict.SOURCE_UNAVAILABLE)
                    notes.append(f"{sid}: fetch failed ({failure})")
                    continue
                hashes[sid] = hashlib.sha256(text.encode()).hexdigest()
                try:
                    review = self.judge.judge(claim=claim.text, source_text=text, source_url=url)
                    if not isinstance(review, SourceReview):
                        review = SourceReview.model_validate(review)
                    verdict = review.verdict
                    if verdict in (VerificationVerdict.SUPPORTED, VerificationVerdict.CONTRADICTED):
                        if not excerpt_is_in_source(review.verbatim_excerpt, text):
                            verdict = VerificationVerdict.INSUFFICIENT
                            notes.append(f"{sid}: judge excerpt absent/too short")
                        else:
                            excerpts[sid] = whitespace_normalize(review.verbatim_excerpt)[:500]
                    if review.rationale:
                        notes.append(f"{sid}: {review.rationale[:350]}")
                    per_source.append(verdict)
                except Exception as exc:
                    per_source.append(VerificationVerdict.INSUFFICIENT)
                    notes.append(f"{sid}: judge failed ({type(exc).__name__})")
            votes = set(per_source)
            if VerificationVerdict.SUPPORTED in votes and VerificationVerdict.CONTRADICTED in votes:
                combined = VerificationVerdict.CONFLICTING
            elif VerificationVerdict.CONTRADICTED in votes:
                combined = VerificationVerdict.CONTRADICTED
            elif VerificationVerdict.SUPPORTED in votes:
                combined = VerificationVerdict.SUPPORTED
            elif votes == {VerificationVerdict.SOURCE_UNAVAILABLE}:
                combined = VerificationVerdict.SOURCE_UNAVAILABLE
            else:
                combined = VerificationVerdict.INSUFFICIENT
            checks.append(ClaimVerification(
                claim_id=claim.claim_id, verdict=combined, source_ids_checked=checked,
                source_sha256=hashes, excerpts=excerpts, notes=notes,
            ))
        return VerificationReport(researched_company=report.identity.canonical_name or report.identity.input_name,
                                  verified_at=datetime.now(timezone.utc), checks=checks,
                                  partial=len(facts) > self.max_claims)
