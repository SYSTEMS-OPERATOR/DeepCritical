# PRIME Flow

The PRIME flow replicates the Protein Research Intelligent Multi-Agent Environment. It is
designed for protein design, hypothesis testing, and reasoning tasks that require
specialised parsing, planning, and execution stages.

## Enabling PRIME

Toggle the flow via Hydra overrides:

```bash
uv run deepresearch flows.prime.enabled=true question="Design a neutralising antibody"
```

You can also start from preset configs such as `bioinformatics_example_configured.yaml`
which enable PRIME-oriented datasets and prompts.

## Node Sequence

When PRIME is enabled the Plan node routes to three dedicated nodes:

1. **`PrimeParse`**: converts the question into a `StructuredProblem` suitable for PRIME
   workflows, enriching it with metadata and hypothesis scaffolding.
2. **`PrimePlan`**: produces a PRIME-specific workflow DAG and stores it on the shared
   state.
3. **`PrimeExecute`**: invokes PRIME tools through the registry, collects execution
   artefacts, and records them in the execution history.
4. **`PrimeEvaluate`**: aggregates results, runs hypothesis validation, and pushes the
   final answer onto `state.answers` for downstream synthesis.

These nodes combine PRIME prompts, the shared `ToolRegistry`, and execution history to
ensure runs remain inspectable and deterministic.

## Configuration Hooks

Key configuration flags for PRIME include:

- `flows.prime.params.manual_confirmation`: require manual approval before executing each
  PRIME step.
- `flows.prime.params.adaptive_replanning`: enable adaptive adjustments when failures are
  detected in the execution history.
- `flows.prime.params.hypothesis_tests`: control which hypothesis datasets are generated
  during execution.

Inspect the `configs/bioinformatics/` and `configs/deep_agent/` groups for advanced
examples that extend PRIME with domain-specific datasets and data loaders.

## Tooling

PRIME draws on the shared `ToolRegistry` under `DeepResearch/src/utils/tool_registry.py`.
Ensure any new PRIME tool specs are registered by the modules imported at the top of
`DeepResearch.app` so they are available when the graph initialises.
