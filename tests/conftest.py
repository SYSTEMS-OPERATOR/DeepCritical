from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional

import pytest


@dataclass
class FakeModel:
    """Simple fake model that returns canned responses for prompts."""

    responses: Optional[Dict[str, str]] = None

    def invoke(self, prompt: str, **_: object) -> str:
        if self.responses and prompt in self.responses:
            return self.responses[prompt]
        return "OK"


@pytest.fixture
def fake_model() -> FakeModel:
    """Provide a fake model for tests that need deterministic output."""

    return FakeModel()
