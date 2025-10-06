# Bioinformatics Flow

The bioinformatics flow focuses on multi-source data fusion, gene/protein reasoning, and
literature synthesis. It extends the PRIME toolchain with domain-specific prompts and
fusion utilities.

## Enabling Bioinformatics Mode

```bash
uv run deepresearch flows.bioinformatics.enabled=true \
    question="Summarise recent findings about TP53 regulation"
```

The repository includes example overrides under `configs/bioinformatics/` to preload GO
annotations, knowledge graph parameters, and dataset loaders.

## Node Responsibilities

- **`BioinformaticsParse`**: maps the question into a `ReasoningTask`, selecting relevant
datasets and enrichment strategies.
- **`BioinformaticsFuse`**: combines gene ontology, literature, and structural insights,
  returning a fused dataset and reasoning summary.

The final synthesis step is shared with the default REACT loop, ensuring results are
aggregated alongside other execution metadata.

## Configuration Tips

- Use `flows.bioinformatics.params.enable_data_fusion=true` to activate the multi-source
  fusion pipeline.
- Adjust `flows.bioinformatics.params.literature_sources` to control which corpora are
  queried.
- Combine with `workflow_orchestration` presets to orchestrate nested hypotheses or spawn
  supporting subflows (for example, enabling DeepSearch inside a bioinformatics run).
