# Graph & Nodes

The DeepCritical runtime is implemented as a `pydantic_graph.Graph` that wires together
explicit node classes declared in `DeepResearch.app`. Each node operates on a shared
`ResearchState` dataclass, allowing the workflow to capture configuration, agent output,
and orchestration metadata without relying on globals.

## ResearchState

`ResearchState` tracks the user question, planned tool invocations, accumulated notes,
agent outputs, orchestration state, and adaptive REACT settings. Nodes rely on this state
rather than re-reading configuration or allocating new coordination helpers.

```python
@dataclass
class ResearchState:
    question: str
    plan: Optional[List[str]] = field(default_factory=list)
    full_plan: Optional[List[Dict[str, Any]]] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)
    answers: List[str] = field(default_factory=list)
    # ... additional orchestration fields trimmed for brevity ...
```

Refer to the source for the complete set of fields, including nested orchestration and
loss-driven controls.

## Planning and Flow Selection

The `Plan` node is the entry point for every run. It inspects the Hydra configuration to
work out which flow should execute:

1. Enhanced REACT modes (`app_mode`) short-circuit to the
   `EnhancedREACTWorkflow` node.
2. Primary workflow orchestration enables the `PrimaryREACTWorkflow` node.
3. Challenge, PRIME, Bioinformatics, RAG, and DeepSearch flows are selected in turn when
their `flows.<name>.enabled` flag is true.
4. If no specialised flow is active, the parser and planner agents cooperate to build a
   basic plan for the search/execution pipeline.

Because this logic lives in a single node, adding a new flow requires only a new config
flag and a new node class.

## Default REACT Loop

When no specialist flow is enabled, the runtime executes the classic REACT sequence:

- **Plan**: parser and planner agents decompose the question into a structured plan.
- **Search**: an executor agent runs each step, storing `ExecutionHistory` details in the
  shared state.
- **Analyze**: summarises execution results and records a high-level metric.
- **Synthesize**: produces the final answer by selecting the most relevant artefact from
  the execution bag.

Each of these nodes is intentionally small and deterministic so that swapping in a
custom agent or registry implementation is straightforward.

## DeepSearch Subgraph

If any of the DeepSearch-style flags are enabled (`flows.deepsearch`, `flows.jina_ai`, or
`flows.node_example`), the graph routes to `DSPlan`. This node delegates to the
`Orchestrator` helper to determine which DeepSearch subgraphs should participate and then
reuses the parser/planner agents to create a web-oriented plan. Execution mirrors the
default REACT loop but provides additional analysis and synthesis nodes tailored for web
search output.

## PRIME and Bioinformatics Flows

The PRIME and Bioinformatics flows follow a similar pattern: dedicated parse, plan, and
execute nodes construct the appropriate structured problem, call the PRIME tool registry,
and gather evaluation metrics. Because they inherit from the same `BaseNode` interface as
other nodes, they can reuse shared utilities such as execution history and orchestration
state.

## Running the Graph

`run_graph` creates all node instances, builds a `Graph`, and executes from the `Plan`
node under a fresh event loop. This keeps CLI execution predictable and sidesteps module
import side effects.

```python
def run_graph(question: str, cfg: DictConfig) -> str:
    state = ResearchState(question=question, config=cfg)
    nodes = (
        Plan(),
        Search(),
        Analyze(),
        Synthesize(),
        # ... specialised flow nodes omitted ...
    )
    g = Graph(nodes=nodes)
    result = loop.run_until_complete(g.run(Plan(), state=state, deps=None))
    return (result.output or "") if hasattr(result, "output") else ""
```

When adding a new node, remember to include it in the `nodes` tuple so that the runtime
can instantiate and cache it before execution begins.
