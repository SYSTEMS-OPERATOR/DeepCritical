# Developer Guide

## Local Environment

1. Install uv and sync dependencies:
   ```bash
   uv sync --all-extras
   ```
2. Activate the environment when running ad-hoc commands:
   ```bash
   source .venv/bin/activate  # uv creates .venv by default
   ```

## Testing

- Run the full suite with coverage:
  ```bash
  uv run pytest --cov=DeepResearch --cov-report=term-missing
  ```
- Mark long-running or network-dependent tests with `@pytest.mark.slow` and skip them by default.
- Use the fake model fixture (`fake_model`) to simulate LLM behaviour without external calls.

## Code Quality

- Format using Black (88 columns) and lint with Ruff before opening a pull request.
- Keep type hints strict enough for `mypy --strict` to succeed; silence unavoidable false positives with targeted `# type: ignore` comments and rationale.
- Enforce import acyclicity with `pycycle --package DeepResearch`.

## Documentation

- Add new pages under `docs/` and update `mkdocs.yml` navigation.
- Document public classes and functions with Google- or NumPy-style docstrings for mkdocstrings rendering.
