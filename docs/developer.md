# Developer Guide

This guide documents local development conventions so new contributors can be productive quickly.

## Environment setup

```bash
uv sync
uv run mkdocs serve  # live-reload documentation
uv run deepresearch question="What are the PRIME stages?"
```

- Use `uv run` to execute tooling (pytest, ruff, mypy, mkdocs) so dependency resolution stays consistent with `uv.lock`.
- The repository pins dependencies through [`pyproject.toml`](../pyproject.toml) and `uv.lock`; commit both when adding packages.

## Coding standards

- Format with `black` and lint with `ruff` (see `[tool.black]` and `[tool.ruff]` in `pyproject.toml`).
- Type-check with `mypy --strict` and install missing stub packages when prompted.
- Write docstrings using Google or NumPy style so mkdocstrings can render arguments and return types automatically.

## Testing and quality gates

- Keep new tests offline by default; mark network or slow tests with `@pytest.mark.slow` so CI can skip them.
- Run `uv run pytest` locally before pushing to ensure coverage metrics remain healthy.
- The CI workflow (`.github/workflows/ci.yml`) also runs linting, typing, security scans, and documentation builds across Python 3.10–3.13.

## Documentation workflow

- Edit content in `docs/` and build locally with `uv run mkdocs serve` or `uv run mkdocs build`.
- Reference modules in the API section using `mkdocstrings` directives (see `docs/api/deepresearch.md`).
- Capture screenshots when changing the visual design of the site and attach them to pull requests.

## Contribution checklist

1. Update the relevant documentation page (including the [CHANGELOG](../CHANGELOG.md) if behaviour changes).
2. Run the automated checks locally (`uv run ruff check .`, `uv run mypy .`, `uv run pytest`).
3. Ensure new modules are imported in `DeepResearch/app.py` if they need to register tools during startup.
4. Request a review and link to any MkDocs preview or screenshots for quick validation.
