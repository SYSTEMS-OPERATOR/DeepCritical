# DeepSearch Flow

The DeepSearch flow adapts the default REACT sequence for open web research. It can be
triggered by enabling any of the DeepSearch flags: `flows.deepsearch`, `flows.jina_ai`, or
`flows.node_example`.

## Enabling DeepSearch

```bash
uv run deepresearch flows.deepsearch.enabled=true \
    question="Map emerging approaches to agentic literature review"
```

To mix experimental prompts or subgraphs, explore the `configs/deepsearch/` and
`configs/deep_agent/` packages.

## Node Lifecycle

1. **`DSPlan`**: asks the `Orchestrator` helper to build a DeepSearch plan based on the
   active flags, then reuses the parser and planner agents to create a tool sequence.
2. **`DSExecute`**: runs the generated plan while keeping an execution history of every
   web search, summarisation, and citation tool call.
3. **`DSAnalyze`**: inspects execution artefacts to extract high-signal documents and
   metadata for synthesis.
4. **`DSSynthesize`**: compiles a narrative that emphasises source attribution and any
   follow-up questions worth exploring.

These nodes can run alongside nested orchestration, enabling scenarios such as PRIME
invoking DeepSearch for literature scouting.

## Tips

- Combine DeepSearch with `app_mode=multi_level_react` to add nested reflection loops.
- Toggle `flows.jina_ai.enabled=true` to swap in the Jina search preset.
- Use `workflow_orchestration` configs to cap runtime or restrict the number of spawned
  subflows when running in CI.
