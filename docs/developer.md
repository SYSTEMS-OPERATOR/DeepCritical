# Developer Guide

This guide captures the day-to-day workflows for contributing to DeepCritical.

## Environment Setup

```bash
# Install dependencies using uv (creates .venv automatically)
uv sync

# Activate the environment for ad-hoc commands
source .venv/bin/activate  # or `uv run <cmd>` to execute without activation
```

Use Python 3.10 or newer. The repository tracks dependencies in `pyproject.toml` and
`uv.lock` for reproducibility.

## Formatting and Linting

- `uv run ruff check .`
- `uv run black .`
- `uv run mypy --config-file pyproject.toml`

CI runs these checks automatically; keeping them green locally reduces review friction.

## Running Tests

The test suite is designed to run fully offline. Execute a focused subset or the entire
suite with:

```bash
uv run pytest
```

Slow or networked scenarios should be marked appropriately so they can be skipped in CI.

## Documentation Workflow

MkDocs powers the documentation site:

```bash
# Build the site once
uv run mkdocs build

# Start a live-reload server on localhost:8000
uv run mkdocs serve -a localhost:8000
```

Docs live under `docs/` and the navigation is configured in `mkdocs.yml`. mkdocstrings is
enabled for future API reference pages—add `::: module.path` directives where you want
API documentation to appear.

## Making Changes

1. Create a feature branch (`codex/docs-*` is the preferred prefix for documentation
   updates).
2. Commit logically grouped changes with descriptive messages.
3. Update `CHANGELOG.md` under the “Unreleased” section when user-facing behaviour
   changes.
4. Open a pull request and include relevant screenshots or logs if you touched the docs or
   CI.

Following these practices keeps the project approachable for new contributors and reduces
regression risk.
