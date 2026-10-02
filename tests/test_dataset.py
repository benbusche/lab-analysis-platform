import pandas as pd
import numpy as np
import pytest

from lap.data.dataset import Dataset
from lap.data.loader import load_csv


def test_dataset_stores_data():
    """Store the provided DataFrame on a Dataset."""
    data = load_csv("examples/sample_data/test.csv")
    dataset = Dataset(data)

    assert dataset.data.equals(data)


def test_dataset_requires_dataframe():
    """Reject values that are not pandas DataFrames."""
    with pytest.raises(TypeError):
        Dataset("not a dataframe")

def test_dataset_column():
    """Return a named column's values as a NumPy array."""
    data = load_csv("examples/sample_data/test.csv")
    dataset = Dataset(data)
    assert isinstance(dataset.column("position"), np.ndarray)
    assert dataset.column("time").tolist() == [0.0, 0.1, 0.2, 0.3]
    assert dataset.column("position").tolist() == [0.12, 0.31, 0.54, 0.81]

def test_dataset_columns():
    """Return all column names in their original order."""
    data = load_csv("examples/sample_data/test.csv")
    dataset = Dataset(data)
    assert dataset.columns() == ["time","position"]

def test_independent():
    """Read the selected independent column and allow changing it."""
    data = load_csv("examples/sample_data/test.csv")
    dataset = Dataset(data, independent_column="position")
    assert dataset.independent().tolist() == [0.12, 0.31, 0.54, 0.81]
    dataset.set_independent(0)
    assert dataset.independent().tolist() == [0.0, 0.1, 0.2, 0.3]

def test_independent_must_be_numeric():
    """Reject a non-numeric independent column."""
    data = pd.DataFrame({"label": ["a", "b", "c"], "value": [1.0, 2.0, 3.0]})
    with pytest.raises(TypeError):
        Dataset(data, independent_column="label")

def test_set_independent_invalid():
    """Reject unknown names, out-of-range indices, and unsupported types."""
    data = load_csv("examples/sample_data/test.csv")
    dataset = Dataset(data)
    with pytest.raises(ValueError):
        dataset.set_independent("nonexistent_column")
    with pytest.raises(ValueError):
        dataset.set_independent(10)
    with pytest.raises(TypeError):
        dataset.set_independent(3.14)

def test_validate_dataset():
    """Validate dataset dimensions, content, types, and column names."""
    # Test with valid dataset
    data = load_csv("examples/sample_data/test.csv")
    dataset = Dataset(data)
    dataset.validate()  # Should not raise any exceptions

    # Test with less than 2 columns
    data_invalid = pd.DataFrame({"only_column": [1, 2, 3]})
    with pytest.raises(ValueError):
        Dataset(data_invalid)

    # Test with empty DataFrame
    data_empty = pd.DataFrame()
    with pytest.raises(ValueError):
        Dataset(data_empty)

    # Test with non-numeric independent column
    data_non_numeric = pd.DataFrame({"label": ["a", "b", "c"], "value": [1.0, 2.0, 3.0]})
    with pytest.raises(TypeError):
        Dataset(data_non_numeric, independent_column="label")

    # Test with duplicate column names
    data_duplicate_columns = pd.DataFrame({"time": [0.0, 0.1], "time": [0.2, 0.3]})
    with pytest.raises(ValueError):
        Dataset(data_duplicate_columns)
