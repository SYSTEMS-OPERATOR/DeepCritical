from __future__ import annotations

from DeepResearch.src.datatypes.tool_specs import ToolCategory, ToolSpec
from DeepResearch.src.utils.tool_registry import ToolRegistry


def test_tool_registration_and_listing() -> None:
    registry = ToolRegistry()
    spec = ToolSpec(
        name="echo",
        category=ToolCategory.ANALYSIS,
        input_schema={"text": {"type": "string"}},
        output_schema={"result": {"type": "string"}},
        dependencies=["preprocess"],
    )

    registry.register_tool(spec)

    assert "echo" in registry.list_tools()
    assert registry.get_tool_spec("echo") is spec
    assert registry.get_tool_dependencies("echo") == ["preprocess"]
    summary = registry.get_registry_summary()
    assert summary["total_tools"] == 1
    assert summary["mock_mode"] is True
    assert summary["categories"][ToolCategory.ANALYSIS.value] == ["echo"]


def test_tool_dependency_availability() -> None:
    registry = ToolRegistry()
    spec_a = ToolSpec(
        name="preprocess",
        category=ToolCategory.KNOWLEDGE_QUERY,
        input_schema={},
        output_schema={},
    )
    spec_b = ToolSpec(
        name="analyse",
        category=ToolCategory.ANALYSIS,
        input_schema={},
        output_schema={},
        dependencies=["preprocess", "missing"],
    )
    registry.register_tool(spec_a)
    registry.register_tool(spec_b)

    availability = registry.check_dependency_availability("analyse")

    assert availability == {"preprocess": True, "missing": False}
