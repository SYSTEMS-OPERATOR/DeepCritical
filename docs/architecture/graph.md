# Graph & Nodes

DeepCritical composes its workflows using [Pydantic Graph](https://github.com/pydantic/pydantic-graph). Each node operates on a shared `ResearchState` defined in `DeepResearch.app` and returns the next node to execute.

## ResearchState

The `ResearchState` dataclass aggregates question context, generated plans, orchestration metadata, and per-flow outputs. Nodes mutate this state as they progress through the workflow.

## Node categories

- **Plan** – routes execution to REACT, PRIME, Bioinformatics, or DeepSearch paths based on Hydra configuration flags.
- **PrimaryREACTWorkflow / EnhancedREACTWorkflow** – orchestrate nested graphs and loss-driven loops.
- **Flow-specific nodes** – `PrimeParse`, `PrimeExecute`, `BioinformaticsParse`, `DSPlan`, etc. implement domain-specific logic.

## Extending the graph

1. Add new node classes under `DeepResearch/app.py` or dedicated modules.
2. Update the graph construction in `run_graph` to include the new nodes.
3. Document the node and its configuration toggles in this docs site.
4. Write offline unit tests that assert routing behaviour without requiring live models.
