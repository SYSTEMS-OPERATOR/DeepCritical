# DeepCritical Overview

DeepCritical is a Hydra-configured, Pydantic Graph powered research agent that implements PRIME-style multi-stage workflows for scientific discovery. The project combines structured tool orchestration, autonomous reasoning loops, and reproducible configuration management so that teams can run advanced experiments locally or in CI.

## Highlights

- **Hydra configuration** for switching between single-step REACT, nested orchestration, and loss-driven optimisation modes.
- **Pydantic Graph orchestration** that captures state transitions across parser, planner, executor, and evaluator nodes.
- **Pydantic AI agents** with a shared tool registry designed for deterministic offline testing.
- **Flow presets** for PRIME protein engineering, bioinformatics data fusion, deep web research, and experimental challenge modes.

## Getting Started

1. Install dependencies with `uv sync`.
2. Run the CLI entrypoint: `uv run deepresearch question="What is deep research?"`.
3. Explore configuration examples in [`configs/`](../configs/).
4. Review the rest of this documentation for architectural deep-dives and workflow recipes.

For quick CLI recipes and configuration toggles see the [CLI guide](cli.md) and [Configuration](configuration.md) sections.
