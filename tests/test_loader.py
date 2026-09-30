import pytest

from lap.data.loader import load_csv, DataLoadError

def test_load_csv():
    data = load_csv("examples/sample_data/projectile.csv")

    assert len(data) == 29

def test_load_missing_file():
    with pytest.raises(FileNotFoundError):
        load_csv("does_not_exist.csv")

def test_load_empty_csv():
    with pytest.raises(DataLoadError):
        load_csv("examples/sample_data/empty.csv")