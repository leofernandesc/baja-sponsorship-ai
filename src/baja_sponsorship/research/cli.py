"""Private local research CLI. Exactly one business input: company name."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from uuid import uuid4

from .openai_provider import OpenAIWebResearchProvider
from .service import ResearchService


def main() -> int:
    parser = argparse.ArgumentParser(description="Research a company for BAJA UEA (E2 draft)")
    parser.add_argument("company_name", help="The sole required business input")
    args = parser.parse_args()

    # The report may contain prospect-specific information. Store privately,
    # in an ignored local directory by default; do not print raw report data.
    report = ResearchService(OpenAIWebResearchProvider.from_environment()).run(args.company_name)
    output_dir = Path("outputs/research")
    output_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
    destination = output_dir / f"research_{uuid4().hex}.json"
    fd = os.open(destination, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as stream:
        stream.write(report.model_dump_json(indent=2))
        stream.write("\n")
    print(f"Research saved to {destination} | identity={report.identity.status.value} | "
          f"source_count={len(report.sources)} | draft_claims={len(report.claims)}")
    print("All claims require independent support review before outbound use.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
