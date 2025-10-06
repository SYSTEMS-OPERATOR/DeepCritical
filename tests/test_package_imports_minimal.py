import importlib

import DeepResearch


def test_app_module_exposes_main() -> None:
    app_module = importlib.import_module("DeepResearch.app")
    assert hasattr(app_module, "main")


def test_package_has_version_metadata() -> None:
    assert hasattr(DeepResearch, "__all__")
