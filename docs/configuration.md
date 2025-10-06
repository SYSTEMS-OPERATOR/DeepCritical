# Configuration

DeepCritical uses Hydra to manage configuration composition. Defaults live in
`configs/config.yaml`, and additional config groups under `configs/` provide presets for
app modes, flows, workflow orchestration, and integration tests.

## Default Configuration

The base config enables workflow orchestration and defines sensible defaults for retries,
output metadata, and optional vLLM integration tests. Key sections include:

- `question`: default research prompt for smoke runs.
- `workflow_orchestration`: toggles the primary REACT orchestrator and provides
  parameters such as maximum iterations, self-correction, and multi-agent coordination.
- `challenge`: optional challenge mode metadata.
- `flows`: compatibility switches for PRIME, Bioinformatics, RAG, DeepSearch, and example
  nodes.
- `outputs`: controls dataset generation, metadata inclusion, and execution trace export.
- `performance`: toggles caching, parallel execution, and workflow optimisation.
- `vllm_tests`: disabled in CI but configurable for local experimentation.

Inspect `configs/config.yaml` to see the full schema and inline documentation.

## Config Groups

Hydra config groups allow you to layer presets without editing the base file. Useful
examples include:

- `app_modes/`: overrides the `app_mode` parameter for enhanced REACT variants.
- `bioinformatics/`: provides detailed datasets and reasoning prompts for biological
  question answering.
- `deepsearch/`: configures DeepSearch subgraphs and API integrations.
- `workflow_orchestration/`: tunes orchestration policies and nested graph behaviour.
- `rag/`, `challenge/`, and `statemachines/`: supply domain-specific toggles and
  guardrails.

Select a group with `+group/name=option` or `group=name` depending on how the package is
structured. For instance, `uv run deepresearch workflow_orchestration=lightweight` would
load `configs/workflow_orchestration/lightweight.yaml` if present.

## Override Patterns

Hydra supports powerful override syntax:

- `uv run deepresearch manual_confirm=true` — update a scalar value.
- `uv run deepresearch flows.prime.enabled=true` — toggle nested attributes.
- `uv run deepresearch outputs.output_format=markdown` — change enums.
- `uv run deepresearch performance.cache_ttl=0` — disable caching.

You can combine overrides and config groups in a single command. Hydra resolves them in
order from left to right.

## Persisting and Reusing Runs

By default Hydra creates an `outputs/` directory with a copy of the resolved configuration
for each run. To reproduce an experiment:

1. Locate the relevant timestamped folder under `outputs/`.
2. Copy `config.yaml` from that folder back into your overrides directory.
3. Launch `uv run deepresearch --config-dir=/path/to/overrides --config-name=config` to
   rehydrate the same setup.

For automated pipelines, consider checking a curated set of overrides into version
control so that collaborators can replay important experiments exactly.
