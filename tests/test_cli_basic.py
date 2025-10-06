from __future__ import annotations

import subprocess
import sys


def test_cli_help_runs() -> None:
    """The CLI help command should execute without hitting external services."""

    result = subprocess.run(
        [sys.executable, "-m", "DeepResearch.app", "--help"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Hydra" in result.stdout or "deepresearch" in result.stdout
