# PRIME Flow

The PRIME (Protein Research Intelligent Multi-Agent Environment) flow specialises in protein engineering tasks by chaining dedicated parsing, planning, execution, and evaluation nodes.

## Capabilities

- Protein intent detection and structured problem extraction.
- Multi-step plan generation for sequence analysis, structure prediction, and evaluation.
- Tool execution with validation of dependencies and mock runners for offline experimentation.

## Example usage

```bash
uv run deepresearch flows.prime.enabled=true question="Design a therapeutic antibody"
```

## Implementation notes

- PRIME-specific agents live in `DeepResearch/src/agents/prime_*` modules.
- Workflow orchestration is coordinated via `PrimaryWorkflowOrchestrator` and `WorkflowOrchestrationConfig`.
- Update tests under `tests/test_graph_nodes.py` when adding new PRIME routing logic.
