"""E2: auditable public company research. No unsourced external assertions.

An evidence URL proves source traceability, not truth of the claim. Only a
human-reviewed claim is eligible to be shown as a confirmed external fact.
"""
from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, StringConstraints, model_validator


NonEmpty = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=2000)]
ShortName = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=200)]


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class IdentityStatus(str, Enum):
    RESOLVED = "resolved"
    AMBIGUOUS = "ambiguous"
    UNRESOLVED = "unresolved"


class SourceType(str, Enum):
    COMPANY_OFFICIAL = "company_official"
    SAE_OR_UNIVERSITY = "sae_or_university"
    INDEPENDENT_REPORTING = "independent_reporting"
    OTHER = "other"


class ClaimType(str, Enum):
    FACT = "fact"
    INFERENCE = "inference"
    PROPOSAL = "proposal"


class ReviewStatus(str, Enum):
    SOURCE_LINKED = "source_linked"
    REVIEW_REQUIRED = "review_required"
    APPROVED = "approved"
    REJECTED = "rejected"


class EvidenceSource(StrictModel):
    source_id: ShortName
    url: HttpUrl
    title: NonEmpty
    source_type: SourceType
    retrieved_at: datetime
    published_at: datetime | None = None
    origin: str = "external_web"

    @model_validator(mode="after")
    def timestamps_are_aware(self):
        if self.retrieved_at.tzinfo is None:
            raise ValueError("retrieved_at must include timezone")
        if self.published_at and self.published_at.tzinfo is None:
            raise ValueError("published_at must include timezone")
        return self


class CompanyIdentity(StrictModel):
    input_name: ShortName
    status: IdentityStatus
    canonical_name: ShortName | None = None
    official_website: HttpUrl | None = None
    identity_source_ids: list[ShortName] = Field(default_factory=list)
    candidates: list[ShortName] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_resolution(self):
        if self.status is IdentityStatus.RESOLVED:
            if not self.canonical_name or not self.identity_source_ids:
                raise ValueError("resolved identity requires name and evidence")
            if self.candidates:
                raise ValueError("resolved identity must not preserve unresolved candidates")
        elif self.status is IdentityStatus.AMBIGUOUS:
            if len(set(self.candidates)) < 2:
                raise ValueError("ambiguous identity requires two distinct candidates")
            if self.canonical_name:
                raise ValueError("ambiguous identity cannot select a canonical name")
        else:
            if self.canonical_name or self.official_website:
                raise ValueError("unresolved identity cannot assert a company")
        return self


class ResearchClaim(StrictModel):
    claim_id: ShortName
    text: NonEmpty
    claim_type: ClaimType
    evidence_source_ids: list[ShortName] = Field(default_factory=list)
    review_status: ReviewStatus = ReviewStatus.REVIEW_REQUIRED
    reviewer_role: str | None = None

    @model_validator(mode="after")
    def claim_guard(self):
        if self.claim_type is ClaimType.FACT and not self.evidence_source_ids:
            raise ValueError("company fact must be linked to a source")
        if self.review_status is ReviewStatus.APPROVED and self.reviewer_role != "operational_management":
            raise ValueError("only operational management may approve a claim")
        return self


class ResearchReport(StrictModel):
    schema_version: str = "e2.v0.1"
    researched_at: datetime
    identity: CompanyIdentity
    sources: list[EvidenceSource] = Field(default_factory=list)
    claims: list[ResearchClaim] = Field(default_factory=list)
    unknowns: list[NonEmpty] = Field(default_factory=list)
    limitations: list[NonEmpty] = Field(default_factory=list)

    @model_validator(mode="after")
    def cross_reference_guards(self):
        if self.researched_at.tzinfo is None:
            raise ValueError("researched_at must be timezone-aware")
        ids = [source.source_id for source in self.sources]
        if len(set(ids)) != len(ids):
            raise ValueError("source IDs must be unique")
        known_ids = set(ids)
        if any(src not in known_ids for src in self.identity.identity_source_ids):
            raise ValueError("identity references an unknown evidence source")
        claim_ids = [claim.claim_id for claim in self.claims]
        if len(set(claim_ids)) != len(claim_ids):
            raise ValueError("claim IDs must be unique")
        for claim in self.claims:
            if any(sid not in known_ids for sid in claim.evidence_source_ids):
                raise ValueError(f"claim {claim.claim_id} cites an unknown source")
        if self.identity.status is not IdentityStatus.RESOLVED and self.claims:
            raise ValueError("do not assert company claims before resolving identity")
        return self
