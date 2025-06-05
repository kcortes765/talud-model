"""Simple logging setup."""

from __future__ import annotations

import logging
from typing import Optional


_DEF_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"


def get_logger(name: str, level: int = logging.INFO,
               fmt: str = _DEF_FORMAT) -> logging.Logger:
    """Return a configured logger."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(fmt))
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger
