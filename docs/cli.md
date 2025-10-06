# Command Line Interface

The `deepresearch` CLI is the primary entrypoint for launching DeepCritical flows. The script is exposed via the `DeepResearch.app:main` console hook defined in `pyproject.toml`.

## Usage

```bash
uv run deepresearch --help
uv run deepresearch app_mode=single_react flows.deepsearch.enabled=true
```

Each invocation accepts Hydra overrides, allowing you to switch app modes, enable or disable flows, and pass provider-specific settings. Combine overrides with configuration files to create reproducible research workflows.

## Development Notes

For offline or test runs, point the CLI at fake tool adapters and models. Keep CLI tests deterministic by avoiding network calls and injecting stub services.
