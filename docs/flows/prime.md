# PRIME Flow

The PRIME (Protein Research Intelligent Multi-Agent Environment) flow specialises in protein engineering tasks by chaining dedicated parsing, planning, execution, and evaluation nodes.

## Capabilities

- Protein intent detection and structured problem extraction via [`QueryParser`](../DeepResearch/src/agents/prime_parser.py).
- Multi-step plan generation through [`PlanGenerator`](../DeepResearch/src/agents/prime_planner.py) producing a `WorkflowDAG`.
- Tool execution with dependency validation using [`ToolExecutor`](../DeepResearch/src/agents/prime_executor.py) and the central `ToolRegistry`.
- Hypothesis tracking and evaluation orchestrated by [`PrimaryWorkflowOrchestrator`](../DeepResearch/src/agents/workflow_orchestrator.py).

## Configuration

Prime is disabled by default. Enable it by toggling the Hydra flag:

```bash
uv run deepresearch flows.prime.enabled=true question="Design a therapeutic antibody"
```

This loads defaults from [`configs/flows/prime.yaml`](../configs/flows/prime.yaml) and wires additional nodes (`PrimeParse`, `PrimeExecute`) into the graph.

## Research loop

1. **Parse.** `PrimeParse` creates a `StructuredProblem` capturing scientific intent, input/output requirements, and constraints.
2. **Plan.** `PlanGenerator` expands the problem into ordered tasks and dependencies (stored on `ResearchState.workflow_dag`).
3. **Execute.** `ToolExecutor` runs through the plan, leveraging both mock tools (`mock_tools.py`) and specialised integrations (`workflow_tools.py`, `bioinformatics_tools.py`) depending on configuration.
4. **Evaluate.** Results feed into orchestration heuristics that determine whether to spawn follow-up workflows or terminate.

When adding new tools or analyses, update the Hydra config to expose toggles, extend the relevant tool modules, and document the behaviour here for quick discoverability.
