"""Utilities for loading configuration settings."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def load_settings(path: str | Path) -> Dict[str, Any]:
    """Load settings from a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
