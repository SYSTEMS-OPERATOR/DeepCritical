import pytest


class FakeModel:
    """Lightweight stand-in for language models used in offline tests."""

    def __init__(self, responses: dict[str, str] | None = None) -> None:
        self._responses = responses or {}

    def invoke(self, prompt: str, **_: object) -> str:
        return self._responses.get(prompt, "OK")


@pytest.fixture
def fake_model() -> FakeModel:
    return FakeModel()


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--runslow", action="store_true", default=False, help="run slow tests")


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "slow: mark tests that require explicit opt-in")
    config.addinivalue_line("markers", "network: mark tests that reach external services")


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    if config.getoption("--runslow"):
        return
    skip_marker = pytest.mark.skip(reason="use --runslow to execute slow or network-dependent tests")
    for item in items:
        if "slow" in item.keywords or "network" in item.keywords:
            item.add_marker(skip_marker)
