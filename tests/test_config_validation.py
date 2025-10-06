from pathlib import Path

from omegaconf import OmegaConf

CONFIG_ROOT = Path(__file__).resolve().parents[1] / "configs"
APP_MODES = {
    "single_react": CONFIG_ROOT / "app_modes" / "single_react.yaml",
    "multi_level_react": CONFIG_ROOT / "app_modes" / "multi_level_react.yaml",
    "nested_orchestration": CONFIG_ROOT / "app_modes" / "nested_orchestration.yaml",
    "loss_driven": CONFIG_ROOT / "app_modes" / "loss_driven.yaml",
}


def test_app_mode_configs_present() -> None:
    missing = [mode for mode, path in APP_MODES.items() if not path.exists()]
    assert not missing, f"missing config files: {missing}"


def test_app_mode_identity_matches_filename() -> None:
    for mode, path in APP_MODES.items():
        cfg = OmegaConf.load(path)
        assert cfg.get("app_mode") == mode
