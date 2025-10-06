# Command Line Interface

The `deepresearch` CLI wraps Hydra to run research flows. Core usage patterns:

- Show available options:
  ```bash
  uv run deepresearch --help
  ```
- Launch the single React flow:
  ```bash
  uv run deepresearch app_mode=single_react flows.prime.enabled=true
  ```
- Execute nested orchestration with DeepSearch enabled:
  ```bash
  uv run deepresearch app_mode=nested_orchestration flows.deepsearch.enabled=true
  ```

When scripting experiments, persist overrides to YAML and reference them with `--config-dir` and `--config-name` flags per Hydra conventions.
