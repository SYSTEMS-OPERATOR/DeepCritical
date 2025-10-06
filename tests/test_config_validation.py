from __future__ import annotations

from pathlib import Path

import pytest
from omegaconf import OmegaConf

from DeepResearch.src.datatypes.workflow_orchestration import AppMode

CONFIG_PATH = Path(__file__).resolve().parents[1] / "configs" / "config.yaml"


def test_default_config_loads() -> None:
    """Baseline Hydra configuration should load without errors."""

    cfg = OmegaConf.load(CONFIG_PATH)
    assert "flows" in cfg
    assert cfg.flows.prime.enabled is not None
    assert cfg.flows.bioinformatics.enabled is not None


@pytest.mark.parametrize(
    ("mode", "expected"),
    [
        ("single_react", AppMode.SINGLE_REACT),
        ("multi_level_react", AppMode.MULTI_LEVEL_REACT),
        ("nested_orchestration", AppMode.NESTED_ORCHESTRATION),
        ("loss_driven", AppMode.LOSS_DRIVEN),
    ],
)
def test_app_mode_enum_contains_expected_modes(mode: str, expected: AppMode) -> None:
    """Ensure the AppMode enum stays in sync with documented CLI options."""

    assert AppMode(mode) is expected
