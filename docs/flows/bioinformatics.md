# Bioinformatics Flow

The bioinformatics flow specializes the agent stack for genomic and proteomic analysis tasks. It integrates domain tools for sequence retrieval, annotation inspection, and hypothesis tracking.

Activate the flow with:

```bash
uv run deepresearch flows.bioinformatics.enabled=true
```

When extending the flow, ensure each tool interaction is mockable and document any new configuration knobs in `docs/configuration.md`.
