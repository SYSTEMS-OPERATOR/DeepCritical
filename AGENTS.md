# DeepCritical • CODEX Project Directive (AGENTS.md)

## Mission
You are the repository’s coding agent. Your priority is to:
1. Stand up high-quality documentation under `docs/` (MkDocs + mkdocstrings), and
2. Strengthen CI and tests (pytest + coverage + typecheck + lint + security), without breaking runtime flows.

## Context
- Python project with Hydra configs and Pydantic Graph/Pydantic AI orchestration under `DeepResearch/`.
- Entry point is the `deepresearch` CLI with multiple app modes and flow toggles.
- Known fragility: circular imports in some tool modules.
- Tests and `codecov.yml` exist; we want better coverage and deterministic/offline testing.

## Guardrails
- Never commit secrets. Never reach out to the network in tests (use fakes/mocks/recordings).
- Prefer minimal diffs. Keep style consistent (black/ruff). Add docstrings where missing.
- For any refactor, create incremental PRs per concern (docs, tests, CI) rather than a mega-PR.
- If you introduce a new dependency, justify it in the PR description and pin it in `pyproject.toml`.

## Deliverables & Acceptance
1. **Docs** (`docs/`, `mkdocs.yml`):
   - Pages: Overview, Architecture, Flows (PRIME, Bioinformatics, DeepSearch), Configuration (Hydra), CLI, Developer Guide, API (mkdocstrings).
   - Local build: `uv run mkdocs build` must succeed. Link check passes.
2. **CI** (`.github/workflows/`):
   - Jobs: lint (ruff/black), typecheck (mypy), test (pytest with coverage), audit (pip-audit + bandit), docs (build).
   - Matrix over Python 3.10–3.13 on Ubuntu; use `astral-sh/setup-uv`.
   - Upload coverage to Codecov.
3. **Tests** (`tests/`):
   - Add offline unit tests for tool registry, node transitions, config validation, and CLI smoke tests using a **fake LLM**.
   - Mark slow/network tests with `@pytest.mark.slow` and skip by default.
   - Coverage target (statement): **≥80%**, file-level checks allowed to start at lower thresholds if complex.
4. **Quality**:
   - `ruff` clean; black-formatted; `mypy --strict` passes (with pydantic plugin if needed).
   - No circular imports (enforced via CI step).
5. **Docs PR** and **CI PR** should include screenshots (docs site local run) and CI run logs.

## Preferred Workflow
- Work in branches: `codex/docs-*`, `codex/ci-*`, `codex/tests-*`.
- Make small, reviewable PRs; request review from maintainers.
- Add or update `CHANGELOG.md` entries under “Unreleased”.

## Step-by-step Tasks (you may execute iteratively)
1. **Docs bootstrap**: add `mkdocs.yml` + `docs/` skeleton + mkdocstrings. Auto-generate API ref stubs.
2. **CI pipeline**: add `ci.yml` with uv setup, lint/type/test/coverage/audit/jobs; `docs.yml` to build docs (and optionally deploy on default branch).
3. **Test scaffolding**: add `tests/test_cli_basic.py`, `tests/test_config_validation.py`, `tests/test_graph_nodes.py`, `tests/test_tool_registry.py`, fixtures for fake model & offline IO.
4. **Circular import check**: add a `pycycle` (or equivalent) step; fail on cycles in `DeepResearch/`.
5. **Polish**: add `pre-commit` config; ruff/black/isort/mypy sections in `pyproject.toml` if missing; tighten `pytest.ini`.

## Commands to try (local)
- `codex "Generate MkDocs config and a docs skeleton using mkdocstrings; wire into pyproject; add docs section to README"`
- `codex "Add a GitHub Actions CI using uv with lint/type/test/coverage and upload to Codecov"`
- `codex "Create a fake LLM and offline tests for the deepresearch CLI covering app modes"`

## CI Automation (non-interactive)
When running in CI, use:  
`codex exec --full-auto "update CHANGELOG and fix ruff/mypy warnings introduced in this PR"`

## Style & Conventions
- Python ≥3.10. Black 88 cols, ruff default rules, mypy strict where feasible.
- Docstrings: Google or NumPy style; include type hints; ensure mkdocstrings renders cleanly.

