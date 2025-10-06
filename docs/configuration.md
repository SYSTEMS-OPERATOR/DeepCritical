# Configuration with Hydra

DeepCritical relies on [Hydra](https://hydra.cc/) to manage configuration across flows, tools, and orchestration modes. The CLI entrypoint in [`DeepResearch/app.py`](../DeepResearch/app.py) is decorated with `@hydra.main`, so it automatically discovers configs under [`configs/`](../configs/).

## Baseline configuration files

| File | Purpose |
| --- | --- |
| `configs/config.yaml` | Default runtime that enables the classic REACT experience. |
| `configs/config_with_modes.yaml` | Adds the `app_mode` switch for enhanced REACT experiments. |
| `configs/workflow_orchestration/*.yaml` | Templates for orchestrator behaviours (e.g. multi-agent or nested loops). |
| `configs/flows/*.yaml` | Flow toggles for PRIME, bioinformatics, DeepSearch, challenge mode, and reference RAG setups. |

Hydra composes these files at runtime, so adding a new flow often means creating a file in `configs/flows/` and enabling it with `+flows.my_flow=enabled`. Use group defaults in `config.yaml` to keep behaviour predictable.

## Overriding values

Hydra exposes every configuration key at the command line:

```bash
uv run deepresearch flows.prime.enabled=true question="Design a therapeutic antibody"
uv run deepresearch app_mode=nested_orchestration hydra.run.dir=.
```

To swap the base config entirely use `--config-name`:

```bash
uv run deepresearch --config-name=config_with_modes question="Map orchestration modes" app_mode=multi_level_react
```

When running in notebooks or tests you can build a `DictConfig` manually using `hydra.compose`. The CLI helpers in [`DeepResearch/app.py`](../DeepResearch/app.py) expect the config object to expose the same structure as the YAML files.

## Output directories

Hydra creates a new output directory per run (default `./outputs/<timestamp>`). For deterministic pipelines set `hydra.run.dir=.` or point it to a temporary directory during tests. This keeps generated artefacts—such as plan JSON, execution logs, or Prime workflow dumps—scoped to a known location.

## Configuration hygiene tips

- Prefer booleans named `enabled` for flow toggles so `Plan.run` can remain declarative.
- Co-locate secrets or credentials with the consuming tool module and document expected environment variables in the relevant docs page.
- Validate new config groups with lightweight unit tests or Pydantic models before wiring them into the orchestration graph.
