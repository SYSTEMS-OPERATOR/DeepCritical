# PRIME Flow

The PRIME flow targets protein engineering and related biomedical research questions. It chains together literature retrieval, structured analysis, and summarization nodes tailored for the PRIME methodology described in the README.

Enable the flow via Hydra overrides:

```bash
uv run deepresearch flows.prime.enabled=true
```

Augment the flow by extending its node graph and providing new domain-specific tools. Keep tests offline by faking responses from external services.
