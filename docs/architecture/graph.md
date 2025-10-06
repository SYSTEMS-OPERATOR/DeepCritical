# Graph & Nodes

DeepCritical composes research workflows through [Pydantic Graph](https://github.com/huggingface/pydantic-graph) definitions. Nodes encapsulate discrete reasoning or tool-execution steps, while edges dictate the transitions driven by agent output and state updates.

Key concepts:

- **State Models:** Typed with Pydantic to ensure deterministic serialization between steps.
- **Node Execution:** Each node receives the current state, performs computation or tool calls, and returns an updated state plus a reference to the next node.
- **Histories:** `ExecutionHistory` captures reasoning traces that can be surfaced in the UI or stored for auditability.

When authoring nodes, prefer pure Python logic that can be covered by unit tests using fake tool adapters or models. Avoid importing heavy integrations at module import time to reduce circular dependency risk.
