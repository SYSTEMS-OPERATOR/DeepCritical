# DeepSearch Flow

DeepSearch provides deep web research capabilities that combine web scraping, summarisation, and citation generation.

## Capabilities

- Query rewriting and expansion to improve recall.
- Web search and scraping via registered tools.
- Summarisation and citation synthesis for downstream use in PRIME or reporting flows.

## Example usage

```bash
uv run deepresearch flows.deepsearch.enabled=true question="Summarise the latest findings on CRISPR"
```

## Implementation notes

- DeepSearch tooling is defined under `DeepResearch/src/tools/` and may depend on external services—mock them in tests.
- When extending DeepSearch, update configuration flags so routing in the `Plan` node remains deterministic.
