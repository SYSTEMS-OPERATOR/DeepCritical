# Agents & Tools

Agents orchestrated by DeepCritical leverage [Pydantic AI](https://github.com/huggingface/pydantic-ai) to manage reasoning loops and tool interactions. Tools are registered through the `ToolRegistry`, allowing flows to declare the capabilities they require.

## Tool Registry

Use the registry to provide a consistent interface across flows. Tools should be injectable, testable, and supply descriptive metadata so that agents can explain their actions.

## Agent Composition

Agents coordinate nodes, execution history, and model providers. Favor dependency injection to keep components modular and to enable offline testing with fake LLMs or mocked services.

Review the README examples for idiomatic usage patterns and adapt them when designing new flow-specific toolkits.
