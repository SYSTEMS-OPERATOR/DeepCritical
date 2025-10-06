# Bioinformatics Flow

The bioinformatics flow fuses multiple scientific data sources—such as GO annotations, literature corpora, and interaction networks—to evaluate biological hypotheses.

## Capabilities

- Parse research questions into structured workflows tailored for bioinformatics tasks.
- Execute specialised tools for sequence, structure, and expression analysis.
- Combine outputs into verifiable reasoning artefacts using evaluator nodes.

## Example usage

```bash
uv run deepresearch flows.bioinformatics.enabled=true question="What is the function of TP53?"
```

## Implementation notes

- Tool specifications live alongside PRIME tools but may require additional dependencies—keep them optional to preserve offline testing.
- Document any external service integrations clearly and mark dependent tests with `@pytest.mark.slow`.
