# DeepSearch Flow

DeepSearch provides deep web reconnaissance capabilities that combine crawling, scraping, and synthesis nodes. The flow is optimized for discovering non-obvious signals across heterogeneous sources.

Enable the flow when running the CLI:

```bash
uv run deepresearch flows.deepsearch.enabled=true
```

For deterministic tests, use recorded HTML fixtures or fake HTTP clients. When introducing new scrapers, avoid circular imports by isolating heavy integrations behind factory functions.
