# Agents & Tools

DeepCritical agents wrap Pydantic AI abstractions and coordinate capabilities through the shared [`ToolRegistry`](../DeepResearch/src/utils/tool_registry.py). The registry loads tool specs during app bootstrap (see the imports at the top of [`DeepResearch/app.py`](../DeepResearch/app.py)) so every flow has consistent metadata about arguments, models, and safety constraints.

## Agent stack

| Component | Location | Purpose |
| --- | --- | --- |
| `ParserAgent` | [`DeepResearch/agents.py`](../DeepResearch/agents.py) | Converts free-form questions into structured prompts consumed by planners. |
| `PlannerAgent` | [`DeepResearch/agents.py`](../DeepResearch/agents.py) | Produces tool plans that the REACT executor can follow step-by-step. |
| `ExecutorAgent` | [`DeepResearch/agents.py`](../DeepResearch/agents.py) | Runs plans against the tool registry, collecting outputs and raising fallbacks when necessary. |
| `ExecutionHistory` | [`DeepResearch/agents.py`](../DeepResearch/agents.py) | Logs tool invocations, intermediate states, and notes for later inspection. |
| PRIME agents | [`DeepResearch/src/agents/prime_*.py`](../DeepResearch/src/agents/) | Specialised components for parsing, planning, executing, and evaluating PRIME workflows. |
| Bioinformatics agents | [`DeepResearch/src/agents/bioinformatics_agents.py`](../DeepResearch/src/agents/bioinformatics_agents.py) | Manage omics-specific parsing, data fusion, and hypothesis evaluation. |
| DeepSearch / RAG agents | [`DeepResearch/src/agents/search_agent.py`](../DeepResearch/src/agents/search_agent.py) and [`rag_agent.py`](../DeepResearch/src/agents/rag_agent.py) | Provide retrieval, ranking, and summarisation logic for online/offline corpora. |

## Tool registry lifecycle

1. **Specification.** Tool specs live under [`DeepResearch/src/tools/`](../DeepResearch/src/tools/). Each module defines `ToolSpec` instances that describe parameters, return types, and safety metadata.
2. **Registration.** Importing the module (for example `mock_tools`, `workflow_tools`, or `pyd_ai_tools`) registers the specs with the singleton `ToolRegistry`. The imports at the top of `app.py` guarantee this happens before any graph runs.
3. **Invocation.** Agents call `registry.get(tool_name)` to retrieve a callable along with a schema. During tests the registry defaults to mock runners so flows remain offline-friendly.
4. **Auditing.** The [`ExecutionHistory`](../DeepResearch/src/utils/execution_history.py) class captures each invocation, enabling reproducibility and loss-driven evaluation loops.

## Adding new tooling

1. Define a `ToolSpec` and optional `ToolRunner` subclass in a new module under `DeepResearch/src/tools/`.
2. Ensure the module is imported during bootstrap so the registry sees the new spec (`app.py` is the typical place).
3. Document configuration knobs (API keys, rate limits, caching) and expose them through Hydra config groups if necessary.
4. Extend the relevant flow documentation page so users understand when and how to enable the tool.
