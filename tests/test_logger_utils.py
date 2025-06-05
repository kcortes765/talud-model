import logging

from src.utils.logger import get_logger


def test_get_logger(capsys):
    logger = get_logger("test_logger")
    logger.info("hello")
    captured = capsys.readouterr()
    # StreamHandler uses stderr by default
    assert "hello" in captured.err
