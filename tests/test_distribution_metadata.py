"""Regression tests for the lumina-auto distribution boundary."""

from __future__ import annotations

import tomllib
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_auto_distribution_metadata_is_distinct_and_import_compatible() -> None:
    metadata = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    project = metadata["project"]
    wheel = metadata["tool"]["hatch"]["build"]["targets"]["wheel"]

    assert project["name"] == "lumina-auto"
    assert project["name"] in project["optional-dependencies"]["dev"][-1]
    assert wheel["packages"] == ["src/lumina"]