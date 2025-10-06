# Command Line Interface

The `deepresearch` CLI is the primary entry point for running DeepCritical workflows. It
is implemented as a Hydra application in `DeepResearch.app`, which means command-line
flags and configuration files are merged at runtime.

## Basic Usage

```bash
# Display Hydra-provided help and default configuration tree
uv run deepresearch --help

# Ask a question with default settings
uv run deepresearch question="What is DeepCritical?"

# Enable the PRIME flow and set a custom question
uv run deepresearch flows.prime.enabled=true question="Engineer a novel protein"
```

Hydra automatically persists each run under `./outputs/DATE/TIME/` with a copy of the
resolved configuration. Inspect these directories to reproduce a specific experiment.

## Selecting App Modes

The `app_mode` parameter toggles between enhanced REACT variants. Valid options include
`single_react`, `multi_level_react`, `nested_orchestration`, and `loss_driven`. Each mode
activates the `EnhancedREACTWorkflow` node, unlocking nested loops, break conditions, and
loss-driven optimisation.

```bash
uv run deepresearch app_mode=multi_level_react \
    question="Map out DeepCritical's orchestration surfaces"
```

## Enabling Flows

Set the corresponding `flows.<name>.enabled` flag to route to a specialised flow:

- `flows.prime.enabled=true`
- `flows.bioinformatics.enabled=true`
- `flows.deepsearch.enabled=true`
- `flows.rag.enabled=true`
- `flows.node_example.enabled=true`
- `flows.jina_ai.enabled=true`

Only one flow is executed per run. If multiple flags are set the Plan node follows a
priority order (challenge → PRIME → Bioinformatics → RAG → DeepSearch) before falling
back to the default REACT loop.

## Working with Config Files

Hydra allows you to compose named configurations. The repository ships with
`config_with_modes.yaml`, `bioinformatics_example.yaml`, and other presets under the
`configs/` directory.

```bash
uv run deepresearch --config-name=config_with_modes app_mode=loss_driven \
    question="Run the loss-driven variant"
```

You can also point Hydra at an alternate config directory using the standard `HYDRA_FULL_ERROR=1` and `HYDRA_CONFIG_DIR` environment variables if you maintain your own
private overrides.

## Debugging Tips

- Pass `hydra.job.chdir=false` to keep runs in the current working directory when
  debugging local resources.
- Use `uv run deepresearch --cfg job --resolve` to inspect the fully resolved config
  without executing the graph.
- Increase verbosity by setting `hydra.verbose=true` or enabling Python logging via
  `PYTHONWARNINGS=default`.
