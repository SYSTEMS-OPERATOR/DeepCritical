# Graph & Nodes

DeepCritical composes its workflows using [Pydantic Graph](https://github.com/pydantic/pydantic-graph). Every execution starts with the `Plan` node in [`DeepResearch/app.py`](../DeepResearch/app.py), which inspects Hydra configuration flags and returns the next node to run. Each node receives a mutable `ResearchState` instance so the overall workflow behaves like a deterministic state machine.

## ResearchState contract

`ResearchState` is a dataclass that tracks:

- The original question, generated plan, and accumulated notes.
- PRIME artefacts such as `StructuredProblem`, `WorkflowDAG`, and execution results produced by [`prime_parser.py`](../DeepResearch/src/agents/prime_parser.py) and [`prime_executor.py`](../DeepResearch/src/agents/prime_executor.py).
- Workflow orchestration metadata (`WorkflowOrchestrationConfig`, `OrchestrationState`, and spawned subgraphs) when enhanced REACT modes are enabled.
- Loss-driven metrics, nested loop bookkeeping, and agent orchestrator instances for the multi-agent research modes.

Any new node should accept the state object, mutate only the keys it owns, and append useful notes for observability.

## Node categories

| Node | Responsibility |
| --- | --- |
| `Plan` | Routes to the correct flow by reading `app_mode`, `workflow_orchestration.*`, and `flows.*.enabled` flags. |
| `PrimaryREACTWorkflow` | Kicks off the PRIME orchestration graph coordinated by `PrimaryWorkflowOrchestrator`. |
| `EnhancedREACTWorkflow` | Handles nested/multi-level REACT setups using `AgentOrchestrator` and `NestedReactConfig`. |
| `PrimeParse` / `PrimeExecute` | Parse PRIME queries, assemble a `WorkflowDAG`, and run the tool plan through `ToolExecutor`. |
| `BioinformaticsParse` / `BioinformaticsExecute` | Resolve `BioinformaticsWorkflow` agents that fuse multi-omics tools. |
| `DSPlan` / `DSExecute` | Build web or document retrieval plans leveraging DeepSearch tooling. |
| `Search` | Default REACT fallback that chains `ParserAgent`, `PlannerAgent`, and `ExecutorAgent` for general-purpose tool calls. |
| `PrepareChallenge` | Enables the experimental challenge flow gated by `challenge.enabled`. |

The graph is intentionally modular: to add a new domain-specific flow, implement dedicated nodes, register any tool specs, and plug the entry node into the routing logic in `Plan.run`.

## Extending the graph safely

1. Define new nodes as subclasses of `BaseNode[ResearchState]`. Use the existing nodes in [`DeepResearch/app.py`](../DeepResearch/app.py) as reference implementations.
2. Declare any extra state you need directly on `ResearchState` to preserve type checking and mkdocstrings coverage.
3. Register required tools in [`DeepResearch/src/tools/`](../DeepResearch/src/tools/) and import the module in `app.py` so the registry sees them during bootstrap.
4. Update the relevant Hydra config (for example `configs/flows/<new_flow>.yaml`) with a boolean `enabled` flag that `Plan.run` can evaluate.
5. Document the flow in the [Flows section](../flows/prime.md) and add diagrams or pseudo-code snippets if the orchestration is complex.
