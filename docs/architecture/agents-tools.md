# Agents & Tools

DeepCritical agents wrap Pydantic AI models and rely on a shared `ToolRegistry` for executing domain-specific operations.

## Agent stack

- `ParserAgent` – understands questions and extracts structured problems.
- `PlannerAgent` – builds execution plans and fallback strategies.
- `ExecutorAgent` – runs tools in sequence, capturing intermediate outputs.
- `ExecutionHistory` – records tool invocations for auditability and loss-driven loops.

## Tool registry

`DeepResearch.src.utils.tool_registry.ToolRegistry` manages tool specifications and mock runners. By default the registry operates in mock mode, making it safe for offline test execution. Real runners can be registered alongside the specs when integration tests are needed.

## Adding new tools

1. Define `ToolSpec` objects in a module within `DeepResearch/src/tools/`.
2. Register runners that implement the `ToolRunner` interface.
3. Import the module from `DeepResearch/app.py` (or another bootstrap module) to trigger registration on startup.
4. Extend unit tests in `tests/test_tool_registry.py` to cover validation behaviour.
