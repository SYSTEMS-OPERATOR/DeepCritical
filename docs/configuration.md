# Configuration (Hydra)

DeepCritical leverages [Hydra](https://hydra.cc/) to compose runtime configuration. Core entry points live in the `configs/` directory and are grouped into:

- `app_modes/`: presets for single, multi-level, nested, and loss-driven orchestration.
- `deep_agent/`, `workflow_orchestration/`, and flow-specific folders controlling enabled agents, tools, and graph structure.

To launch with a specific mode and flow combination, pass overrides to the CLI:

```bash
uv run deepresearch app_mode=multi_level_react flows.prime.enabled=true
```

Hydra supports configuration sweeps and experiment tracking; see the Developer Guide for recommended directory layouts when adding new YAML files.
