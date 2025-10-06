# DeepCritical Documentation

DeepCritical orchestrates critical research workflows using Hydra-configured applications, Pydantic Graph state management, and Pydantic AI agents. The project bundles reusable flows for PRIME experimentation, bioinformatics analysis, and deep web investigation while providing a single command-line entry point via `deepresearch`.

This documentation complements the repository README by offering deeper architectural context, configuration guidance, and API references for contributors and operators.

## Getting Started

1. Install dependencies with [uv](https://docs.astral.sh/uv/):
   ```bash
   uv sync --all-extras
   ```
2. Run the CLI with the default configuration:
   ```bash
   uv run deepresearch
   ```
3. Explore specific workflows using the Hydra configuration system described in the following sections.

Use the navigation menu to jump to architecture deep-dives, flow-specific guidance, configuration examples, and the developer guide.
