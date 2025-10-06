# Command Line Interface

The `deepresearch` CLI is defined in [`pyproject.toml`](../pyproject.toml) and implemented in [`DeepResearch/app.py`](../DeepResearch/app.py). It provides a single entrypoint for switching orchestration modes, enabling flows, and routing questions to specialised agents.

## Basic usage

```bash
uv run deepresearch --help
uv run deepresearch question="What is PRIME?"
```

The CLI accepts free-form questions through the `question` parameter. Without additional flags it runs the classic REACT flow composed of `ParserAgent`, `PlannerAgent`, and `ExecutorAgent`.

## Selecting orchestration modes

Enhanced REACT modes expose additional automation layers:

```bash
uv run deepresearch app_mode=single_react
uv run deepresearch app_mode=multi_level_react
uv run deepresearch app_mode=nested_orchestration
uv run deepresearch app_mode=loss_driven
```

Each mode configures different orchestrator classes in [`DeepResearch/src/agents/workflow_orchestrator.py`](../DeepResearch/src/agents/workflow_orchestrator.py) and [`DeepResearch/src/agents/agent_orchestrator.py`](../DeepResearch/src/agents/agent_orchestrator.py).

## Enabling domain flows

```bash
uv run deepresearch flows.prime.enabled=true question="Design a therapeutic antibody"
uv run deepresearch flows.bioinformatics.enabled=true question="Fuse multi-omics data"
uv run deepresearch flows.deepsearch.enabled=true question="Summarise current literature"
uv run deepresearch flows.challenge.enabled=true question="Generate benchmarking tasks"
```

These flags mirror files under `configs/flows/` and instruct the `Plan` node to hand off to domain-specific graphs.

## Useful Hydra overrides

- `hydra.run.dir=.` – keep outputs in the current directory (handy for deterministic tests).
- `hydra.job.chdir=false` – prevent Hydra from changing the working directory when you want relative paths to remain intact.
- `logging.level=DEBUG` – enable verbose logging for troubleshooting plan routing.

## Running programmatically

If you need to invoke DeepCritical from Python, import `run_graph` and pass a `DictConfig` yourself:

```python
from omegaconf import OmegaConf
from DeepResearch.app import run_graph

cfg = OmegaConf.load("configs/config.yaml")
cfg.question = "Map emerging protein design techniques"
run_graph(cfg)
```

This mirrors the behaviour of the CLI while giving you full control over configuration composition in notebooks or pipelines.
