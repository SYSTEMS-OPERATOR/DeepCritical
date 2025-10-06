# Command Line Interface

The `deepresearch` CLI is installed via the `pyproject.toml` entry point and acts as the primary interface for running DeepCritical workflows.

## Basic usage

```bash
uv run deepresearch --help
uv run deepresearch question="What is PRIME?"
```

## Selecting modes

```bash
uv run deepresearch app_mode=single_react
uv run deepresearch app_mode=multi_level_react
uv run deepresearch app_mode=nested_orchestration
uv run deepresearch app_mode=loss_driven
```

## Enabling flows

```bash
uv run deepresearch flows.prime.enabled=true question="Design a therapeutic antibody"
uv run deepresearch flows.bioinformatics.enabled=true question="Fuse multi-omics data"
uv run deepresearch flows.deepsearch.enabled=true question="Summarise current literature"
```

## Tips

- Hydra will create a working directory per run; use `hydra.run.dir=.` for deterministic output paths in tests.
- To experiment interactively, run `python -m DeepResearch.app` with the same overrides shown above.
