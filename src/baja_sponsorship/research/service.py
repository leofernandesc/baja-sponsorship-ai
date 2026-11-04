"""Replaceable provider boundary; no Streamlit, external calls, or sponsor terms."""
from __future__ import annotations

from typing import Protocol

from .models import ClaimType, IdentityStatus, ResearchClaim, ResearchReport, ReviewStatus


class ResearchProvider(Protocol):
    def research(self, company_name: str) -> ResearchReport: ...


class ResearchService:
    def __init__(self, provider: ResearchProvider):
        self.provider = provider

    def run(self, company_name: str) -> ResearchReport:
        normalized = " ".join(company_name.split())
        if not (1 <= len(normalized) <= 200):
            raise ValueError("company name must be between 1 and 200 characters")
        report = self.provider.research(normalized)
        if report.identity.input_name.casefold() != normalized.casefold():
            raise ValueError("provider returned evidence for a different input")
        return report


def outgoing_approved_facts(report: ResearchReport) -> list[ResearchClaim]:
    """Only confirmed, management-approved company facts can flow downstream.

    A source URL alone does not imply its claim is true. Real source-text
    validation and manual approval are handled in later E2 checkpoints.
    """
    if report.identity.status is not IdentityStatus.RESOLVED:
        return []
    return [
        claim for claim in report.claims
        if claim.claim_type is ClaimType.FACT
        and claim.review_status is ReviewStatus.APPROVED
        and claim.evidence_source_ids
    ]
