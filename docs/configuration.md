# Configuration with Hydra

DeepCritical relies on [Hydra](https://hydra.cc/) for structured configuration management. Default configuration files live in `configs/` and are referenced by the CLI entrypoint through `@hydra.main` decorators.

## Core configuration files

- `configs/config.yaml` – baseline runtime configuration used by `deepresearch`.
- `configs/config_with_modes.yaml` – enables REACT mode toggles for nested orchestration and loss-driven execution.
- `configs/workflow_orchestration/*.yaml` – presets for advanced orchestration graphs.
- `configs/flows/*.yaml` – individual flow presets (PRIME, bioinformatics, DeepSearch, etc.).

## Overriding values

Hydra lets you override any configuration value from the command line:

```bash
uv run deepresearch flows.prime.enabled=true question="Design a therapeutic antibody"
uv run deepresearch app_mode=multi_level_react question="Analyse loss functions"
```

You can also select alternate configuration files:

```bash
uv run deepresearch --config-name=config_with_modes question="Map orchestration modes" app_mode=nested_orchestration
```

## Tips for contributors

- Keep new configuration groups colocated with existing Hydra directories.
- Document new config options in this docs site and in the module docstrings that consume them.
- When adding new flows, mirror the existing `flows.*.enabled` flags so they remain easy to test offline.
