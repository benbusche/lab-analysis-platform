import pytest

from lap.data.loader import load_csv, DataLoadError

def test_load_csv():
    """Load the sample projectile CSV and check its row count."""
    data = load_csv("examples/sample_data/projectile.csv")
    assert len(data) == 29

def test_load_missing_file():
    """Raise FileNotFoundError for a path that does not exist."""
    with pytest.raises(FileNotFoundError):
        load_csv("does_not_exist.csv")

def test_load_empty_csv():
    """Raise DataLoadError for an empty CSV file."""
    with pytest.raises(DataLoadError):
        load_csv("examples/sample_data/empty.csv")