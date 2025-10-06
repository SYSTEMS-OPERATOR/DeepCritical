# Bioinformatics Flow

The bioinformatics flow fuses multi-omics tooling to analyse biological datasets, validate hypotheses, and surface evidence trails.

## Capabilities

- Domain-aware parsing implemented in [`bioinformatics_agents.py`](../DeepResearch/src/agents/bioinformatics_agents.py) to interpret sequencing, structure, and expression queries.
- Tooling for enrichment analysis, pathway mapping, and evidence retrieval through modules such as [`bioinformatics_tools.py`](../DeepResearch/src/tools/bioinformatics_tools.py) and [`integrated_search_tools.py`](../DeepResearch/src/tools/integrated_search_tools.py).
- Hypothesis assembly using orchestration helpers in [`workflow_orchestrator.py`](../DeepResearch/src/agents/workflow_orchestrator.py).

## Configuration

Enable the flow with:

```bash
uv run deepresearch flows.bioinformatics.enabled=true question="Prioritise targets from RNA-seq and proteomics"
```

The toggle reads defaults from [`configs/flows/bioinformatics.yaml`](../configs/flows/bioinformatics.yaml), which can be extended with dataset handles or analysis preferences.

## Typical execution

1. `BioinformaticsParse` extracts modalities, species, and hypothesis constraints into the `ResearchState`.
2. Task planning orchestrates specialised tool invocations (e.g. enrichment, pathway cross-referencing, literature lookup).
3. Execution collates results from multiple tools and stores them on `ResearchState.execution_results` for downstream reasoning or reporting.

When extending this flow, document new data requirements, configurable cut-offs, and any long-running steps so users can gauge resource needs before enabling the pipeline.
