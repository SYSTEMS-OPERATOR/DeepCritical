# Developer Guide

This guide documents local development conventions so new contributors can be productive quickly.

## Environment setup

```bash
uv sync
uv run pytest
```

- Use `uv run` to execute tooling (pytest, ruff, mypy, mkdocs).
- The repository pins dependencies through `pyproject.toml` and `uv.lock`.

## Coding standards

- Format with `black` and lint with `ruff`.
- Type-check with `mypy --strict` (ignoring third-party imports via configuration).
- Write docstrings using Google or NumPy style to render cleanly in mkdocstrings.

## Testing strategy

- Keep new tests offline by default; mark network or slow tests with `@pytest.mark.slow`.
- Use fixtures in `tests/conftest.py` for fake models or Hydra overrides.
- Maintain coverage at or above 80% for core packages.

## Documentation workflow

- Edit content in `docs/` and build locally with `uv run mkdocs serve` or `uv run mkdocs build`.
- Reference modules in the API reference using `mkdocstrings` directives (see `docs/api/deepresearch.md`).
- Include screenshots in PRs when visual changes are made to the documentation site.

## Automation

- Continuous integration runs linting, typing, testing, audits, and docs builds across Python 3.10–3.13.
- A manual "Codex Exec" workflow is available to run scripted maintenance tasks in CI.
