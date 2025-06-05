from pathlib import Path

from src.utils.config import load_settings


def test_load_settings(tmp_path):
    data = {"foo": 1}
    file = tmp_path / "settings.json"
    file.write_text('{"foo": 1}')
    assert load_settings(file) == data
