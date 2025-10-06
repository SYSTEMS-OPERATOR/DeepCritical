# Graph & Nodes

DeepCritical composes research workflows with [pydantic-graph](https://github.com/pydantic/pydantic-graph) to model directed graphs of nodes. Each node encapsulates a discrete capability (e.g., hypothesis generation, literature review) and exchanges structured state objects validated by Pydantic models.

Key concepts:

- **ExecutionGraph** instances describe permissible transitions between nodes.
- **NodeState** models encode the input/output contract for each node and surface validation errors early.
- **Break conditions** protect long-running loops and ensure bounded execution.

Refer to the API reference for concrete classes such as `DeepResearch.src.graph.execution.ExecutionGraph` and related node implementations. When developing new nodes, prefer deterministic unit tests with fake models to keep the suite offline.
