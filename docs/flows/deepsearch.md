# DeepSearch Flow

The DeepSearch flow focuses on deep web and document retrieval to enrich research questions with up-to-date evidence.

## Capabilities

- Plan construction via `DSPlan`, which inspects Hydra toggles to determine whether to use standard DeepSearch, the node example, or Jina AI integrations.
- Tooling backed by [`deepsearch_tools.py`](../DeepResearch/src/tools/deepsearch_tools.py), [`websearch_tools.py`](../DeepResearch/src/tools/websearch_tools.py), and [`integrated_search_tools.py`](../DeepResearch/src/tools/integrated_search_tools.py).
- Summarisation and aggregation using [`search_agent.py`](../DeepResearch/src/agents/search_agent.py) and [`rag_agent.py`](../DeepResearch/src/agents/rag_agent.py).

## Configuration

Enable DeepSearch or its variants through the Hydra flags:

```bash
uv run deepresearch flows.deepsearch.enabled=true question="Track the latest PRIME publications"
uv run deepresearch flows.node_example.enabled=true question="Run the sandbox node example"
uv run deepresearch flows.jina_ai.enabled=true question="Leverage Jina AI retrievers"
```

Defaults are defined in [`configs/flows/deepsearch.yaml`](../configs/flows/deepsearch.yaml) and related config files for the node example and Jina integrations.

## Offline considerations

Several DeepSearch tools require external connectivity. For deterministic testing:

- Use the mock tool implementations registered in [`mock_tools.py`](../DeepResearch/src/tools/mock_tools.py).
- Disable network-dependent flags or provide cached datasets via configuration.
- Document any credentials or API keys in the contribution guidelines before enabling them in CI.
