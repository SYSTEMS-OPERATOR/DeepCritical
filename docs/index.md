# DeepCritical Overview

DeepCritical is a Hydra-configured research assistant that layers [Pydantic Graph](https://github.com/pydantic/pydantic-graph) orchestration on top of a modular tool ecosystem. It bundles PRIME-style protein engineering agents, deep web research helpers, and experimental orchestration modes behind a single CLI so that scientific exploration can run repeatably in notebooks, terminals, or CI environments.

## Core ideas

- **Composable graphs.** The `run_graph` entrypoint in [`DeepResearch/app.py`](../DeepResearch/app.py) wires Pydantic Graph nodes that cooperatively update a shared `ResearchState` dataclass. Nodes can be swapped or extended without rewriting the orchestration loop.
- **Structured configuration.** Hydra config groups in [`configs/`](../configs/) toggle flows such as PRIME, Bioinformatics, DeepSearch, and nested orchestration patterns so experiments can be reproduced with a single command line flag.
- **Tool-first automation.** Agents resolve capabilities through the central [`ToolRegistry`](../DeepResearch/src/utils/tool_registry.py), ensuring every flow—whether mock, offline, or production—has consistent validation and logging semantics.

## Quick start

1. Install dependencies with `uv sync` (or `pip install -e .` if you prefer standard virtual environments).
2. Run the CLI entrypoint:

   ```bash
   uv run deepresearch question="What is deep research?"
   ```

3. Flip Hydra switches to explore different flows:

   ```bash
   uv run deepresearch flows.prime.enabled=true question="Design a therapeutic antibody"
   uv run deepresearch app_mode=multi_level_react question="Diagnose orchestration states"
   ```

4. Dive deeper using the guides in this documentation:

   - [Architecture](architecture/graph.md) explains the graph and node contract.
   - [Flows](flows/prime.md) profile domain-specific pipelines.
   - [Configuration](configuration.md) captures Hydra override patterns.
   - [CLI](cli.md) collects repeatable command examples.

## Project map

The repository is organised around a few high-signal directories:

| Location | Purpose |
| --- | --- |
| [`DeepResearch/`](../DeepResearch/) | Runtime package containing the graph, agents, tool registry, and orchestration helpers. |
| [`configs/`](../configs/) | Hydra configuration tree used by the CLI and integration tests. |
| [`docs/`](./) | This documentation site (built with MkDocs and mkdocstrings). |
| [`scripts/prompt_testing/`](../scripts/prompt_testing/) | Utilities for evaluating prompt variants offline. |
| [`tests/`](../tests/) | Offline smoke tests and graph validation helpers. |

Keep an eye on the [Developer Guide](developer.md) for coding conventions and automation tips when contributing new flows or tooling.
