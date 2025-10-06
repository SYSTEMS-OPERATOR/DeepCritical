# Developer Guide

This guide highlights practices for extending DeepCritical while preserving deterministic, testable behaviors.

## Environment Setup

1. Install dependencies with `uv sync`.
2. Run formatting and lint checks via `uv run ruff check .` and `uv run black --check .`.
3. Execute tests with `uv run pytest` to confirm flows remain stable.

## Adding New Components

- **Nodes & Graphs:** Implement nodes under `DeepResearch/nodes/` and wire them into Pydantic Graph definitions. Provide unit tests covering transitions and state mutations.
- **Tools:** Register tools with `ToolRegistry` and supply fake implementations for testing.
- **Configs:** Extend Hydra YAML files and update Pydantic configuration models to expose new parameters.

## Quality Bar

Follow the repository guardrails (see `AGENTS.md`): maintain coverage ≥80%, avoid circular imports, and document changes in the changelog. When introducing dependencies, record them in `pyproject.toml` and explain the motivation in the PR description.
