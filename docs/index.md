# DeepCritical Overview

DeepCritical is a Hydra-configured research automation stack that wires Pydantic Graph
state machines together with Pydantic AI agents and an extensible tool registry. It
implements the PRIME (Protein Research Intelligent Multi-Agent Environment) workflow so
that complex biological and open-ended research questions can be decomposed, executed,
and synthesised deterministically. The same orchestration primitives also power
DeepSearch-style web research, a configurable challenge mode, and multiple REACT
variants exposed via the `deepresearch` CLI.

## Key Capabilities

- **Graph-first orchestration.** The runtime graph defined in
  `DeepResearch.app` coordinates planning, execution, synthesis, and
  specialised flows through explicit nodes and edges so behaviour is easy to audit and
  extend.
- **Agent specialisation.** Parser, planner, and executor agents encapsulate
  Pydantic AI prompts and maintain their own execution history, making it simple to
  reuse them across flows or swap in custom tools.
- **Tool registry and execution history.** PRIME tool specifications, mock runners, and
  adaptive execution history tracking live in dedicated utility modules to keep core
  workflows deterministic for local development and CI.
- **Configuration overlays.** Hydra configuration packages toggle PRIME,
  Bioinformatics, DeepSearch, and orchestration scenarios without touching code, and
  additional overrides can be layered per run.

## Quick Start

```bash
# Install dependencies and create a virtual environment
uv sync

# Ask a question using the default configuration
uv run deepresearch question="What is deep research?"

# Switch to the multi-level REACT loop
uv run deepresearch app_mode=multi_level_react question="Map the DeepCritical stack"

# Enable the PRIME workflow
uv run deepresearch flows.prime.enabled=true question="Design a novel protein binder"
```

When you are ready to customise flows, browse the [Configuration guide](configuration.md)
for Hydra override patterns and additional config groups.

## Documentation Roadmap

- Learn how nodes hand off state and invoke agents in
  [Graph & Nodes](architecture/graph.md).
- Explore the agent layer, tool registry, and execution history utilities in
  [Agents & Tools](architecture/agents-tools.md).
- Review scenario-specific guidance in the [Flows](flows/prime.md) section.
- Understand CLI usage patterns and debugging strategies in the [CLI guide](cli.md).
- Follow the [Developer Guide](developer.md) for environment setup and contribution
  practices.

Each page includes cross-links back to relevant source modules so you can go from
conceptual overviews to implementation details quickly.
