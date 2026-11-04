"""Explicitly opt-in live two-stage research + semantic verification smoke test.

Usage: OPENAI_API_KEY=... OPENAI_MODEL=... python -m baja_sponsorship.research.live_validation Bosch
Costs API usage. Never place the key in command arguments, issues, or git files.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from uuid import uuid4

from .evidence_verifier import EvidenceVerifier
from .http_fetcher import SafePublicSourceFetcher
from .openai_judge import OpenAISourceJudge
from .openai_provider import OpenAIWebResearchProvider
from .service import ResearchService


def main() -> int:
    parser = argparse.ArgumentParser(description="E2 opt-in live API + source-content validation")
    parser.add_argument("company_name", help="Company to research")
    args = parser.parse_args()
    if not os.getenv("OPENAI_API_KEY") or not os.getenv("OPENAI_MODEL"):
        print("BLOCKED: configure OPENAI_API_KEY and OPENAI_MODEL in your private shell first; no API call made.", file=sys.stderr)
        return 2
    from openai import OpenAI
    client = OpenAI(timeout=25.0, max_retries=0)
    # Bounded execution: one web_search Response, one structured extraction, and
    # at most three independent LLM judgments over first-party evidence.
    model = os.environ["OPENAI_MODEL"]
    report = ResearchService(OpenAIWebResearchProvider(client, model, max_sources=8, max_claims=3)).run(args.company_name)
    checker = EvidenceVerifier(SafePublicSourceFetcher(), OpenAISourceJudge(client, model),
                               max_claims=3, max_sources_per_claim=1)
    checked = checker.verify(report)
    destination = Path("outputs/research")
    destination.mkdir(parents=True, exist_ok=True, mode=0o700)
    out = destination / f"live_check_{uuid4().hex}.json"
    payload = {"research": json.loads(report.model_dump_json()),
               "semantic_verification": json.loads(checked.model_dump_json())}
    fd = os.open(out, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print("Identity:", report.identity.status.value, "sources:", len(report.sources),
          "draft claims:", len(report.claims))
    print("Semantic verdicts:", {v.value: sum(c.verdict == v for c in checked.checks)
                                  for v in set(c.verdict for c in checked.checks)})
    print("Private report:", out)
    print("No claim is automatically approved; operational-management review remains required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
