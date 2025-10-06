from __future__ import annotations

from types import SimpleNamespace

import pytest
from omegaconf import OmegaConf

from DeepResearch.app import (
    BioinformaticsParse,
    DSPlan,
    Plan,
    PrimeParse,
    ResearchState,
)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("flow_key", "expected_cls"),
    [
        ("prime", PrimeParse),
        ("bioinformatics", BioinformaticsParse),
        ("deepsearch", DSPlan),
    ],
)
async def test_plan_routes_to_configured_flow(flow_key: str, expected_cls: type) -> None:
    """The Plan node should route directly to enabled flows without invoking live agents."""

    cfg = OmegaConf.create({"flows": {flow_key: {"enabled": True}}})
    state = ResearchState(question="test", config=cfg)
    ctx = SimpleNamespace(state=state)

    next_node = await Plan().run(ctx)  # type: ignore[arg-type]

    assert isinstance(next_node, expected_cls)
