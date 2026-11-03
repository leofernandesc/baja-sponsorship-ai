"""Offline fixtures: synthetic data only, never real company claims."""
from pathlib import Path

from .models import ResearchReport


class JsonFixtureProvider:
    def __init__(self, fixture_path: str | Path):
        self.fixture_path = Path(fixture_path)

    def research(self, company_name: str) -> ResearchReport:
        report = ResearchReport.model_validate_json(self.fixture_path.read_text(encoding="utf-8"))
        return report
