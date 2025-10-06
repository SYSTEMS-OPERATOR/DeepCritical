# Agents & Tools

Agents in DeepCritical are orchestrated through [pydantic-ai](https://github.com/pydantic/pydantic-ai) and rely on tool registries for external actions (e.g., web search, structure prediction). Tool metadata is declared via Pydantic models so orchestration layers can validate availability before execution.

## Tool Registry

The `ToolRegistry` centralises discovery and lifecycle management of tools. It exposes helpers for:

- Registering built-in tools with descriptive metadata.
- Enabling/disabling capabilities per flow through Hydra configuration.
- Injecting mock implementations for offline tests.

## Execution History

`ExecutionHistory` captures agent interactions, including prompts, model outputs, and tool calls. The history is critical for debugging and evaluating flows. Tests should assert that history objects remain serialisable and redact sensitive fields before persistence.
