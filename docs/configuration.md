# Configuration (Hydra)

DeepCritical relies on [Hydra](https://hydra.cc/) for hierarchical configuration. The default configuration tree lives under `configs/` and exposes switches for selecting app modes (`single_react`, `multi_level_react`, `nested_orchestration`, `loss_driven`) and enabling flows (PRIME, Bioinformatics, DeepSearch).

## Override Patterns

Use Hydra's command-line overrides to toggle modes or enable specific flows:

```bash
uv run deepresearch app_mode=multi_level_react flows.prime.enabled=true
```

Configuration groups are organized to keep flow-specific settings isolated from shared infrastructure such as model providers or tool registries. Add new options by extending the relevant YAML file within `configs/` and updating the corresponding Pydantic settings models.

## Tips

- Keep overrides deterministic for tests by providing fake credentials and local resources.
- Document new configuration groups in this section to keep operators aligned with available knobs.
