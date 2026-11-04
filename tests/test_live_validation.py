"""Ensure a real API call is impossible without explicit private configuration."""
import sys
from baja_sponsorship.research.live_validation import main


def test_live_smoke_without_credentials_exits_before_network(monkeypatch, capsys):
    monkeypatch.delenv('OPENAI_API_KEY', raising=False)
    monkeypatch.delenv('OPENAI_MODEL', raising=False)
    monkeypatch.setattr(sys, 'argv', ['baja-live-check', 'Bosch'])
    assert main() == 2
    assert 'BLOCKED' in capsys.readouterr().err
