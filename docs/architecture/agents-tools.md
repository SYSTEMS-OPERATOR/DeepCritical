# Agents & Tools

DeepCritical separates reasoning from execution by pairing Pydantic AI agents with a
mock-friendly tool registry. This section explains how the agent stack is composed and
how tools are discovered, executed, and audited.

## Agent Layer

`DeepResearch/agents.py` defines a hierarchy of Pydantic AI wrappers:

- `BaseAgent` handles model selection, dependency injection, execution bookkeeping, and
  automatic tool registration. It exposes asynchronous and synchronous execution helpers
  so that both graph nodes and standalone scripts can reuse the same logic.
- `ParserAgent` interprets incoming questions and emits structured representations.
- `PlannerAgent` builds workflow DAGs using planner prompts and returns ordered tool
  sequences.
- `ExecutorAgent` (defined alongside specialised agent orchestrators) executes the plan,
  writing results and errors into an `ExecutionHistory` instance for later analysis.

Every agent records execution status in a shared history object so that failures can be
inspected and downstream nodes can adapt their behaviour.

## Execution History

`ExecutionHistory` keeps a detailed ledger of tool invocations. Each `ExecutionItem`
tracks the tool name, status, results, parameters, timestamps, and retry counts. History
instances provide convenience helpers to:

- Retrieve successful or failed steps.
- Count how often a specific tool has been invoked.
- Summarise run statistics, including success rate and failure patterns.
- Serialise the entire run to disk for post-mortem analysis.

Because nodes and agents exchange a shared history, unit tests can remain fully offline by
injecting deterministic mock results.

## Tool Registry

The global `ToolRegistry` collects PRIME tool specifications and their corresponding
runners. Its responsibilities include:

- Registering tool metadata (`ToolSpec`) with optional runner classes.
- Falling back to mock runners when running in development mode.
- Listing tools by name or category and checking dependency availability.
- Executing a tool or validating parameters without execution.
- Loading additional tools dynamically from Python modules.

Registry summaries highlight how many tools have concrete runners versus mock
implementations, making it easy to audit coverage before enabling live integrations.

## Integrating New Tools or Agents

To add a new capability:

1. Create a `ToolSpec` describing the tool inputs, outputs, and dependencies.
2. Implement a `ToolRunner` that respects the registry contract (or rely on the default
   `MockToolRunner`).
3. Register the tool in a module that is imported by `DeepResearch.app` so that the global
   registry is populated at startup.
4. Update or create an agent that references the new tool and emits structured results.

Following this workflow keeps real integrations opt-in while preserving deterministic
behaviour for local development and CI.
