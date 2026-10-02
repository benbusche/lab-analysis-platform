import pandas as pd
import numpy as np
import pytest

from lap.data.dataset import Dataset
from lap.data.loader import load_csv


def test_dataset_stores_data():
    data = load_csv("examples/sample_data/test.csv")
    dataset = Dataset(data)

    assert dataset.data.equals(data)


def test_dataset_requires_dataframe():
    with pytest.raises(TypeError):
        Dataset("not a dataframe")

def test_dataset_column():
    data = load_csv("examples/sample_data/test.csv")
    dataset = Dataset(data)
    assert isinstance(dataset.column("position"), np.ndarray)
    assert dataset.column("time").tolist() == [0.0, 0.1, 0.2, 0.3]
    assert dataset.column("position").tolist() == [0.12, 0.31, 0.54, 0.81]

def test_dataset_columns():
    data = load_csv("examples/sample_data/test.csv")
    dataset = Dataset(data)
    assert dataset.columns() == ["time","position"]

def test_independent():
    data = load_csv("examples/sample_data/test.csv")
    dataset = Dataset(data, independent_column="position")
    assert dataset.independent().tolist() == [0.12, 0.31, 0.54, 0.81]
    dataset.set_independent(0)
    assert dataset.independent().tolist() == [0.0, 0.1, 0.2, 0.3]
