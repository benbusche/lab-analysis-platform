import pandas as pd
import pytest

from lap.data.cleaning import drop_missing
from lap.data.dataset import Dataset


def test_drop_missing_uses_selected_columns_and_preserves_input():
	"""Drop incomplete selected rows without mutating the original dataset."""
	data = pd.DataFrame(
		{
			"time": [0.0, 1.0, float("nan"), 3.0],
			"measurement": [10.0, 20.0, 30.0, float("nan")],
			"note": [None, "usable", "usable", "usable"],
		},
		index=[10, 20, 30, 40],
	)
	dataset = Dataset(data, independent_column="time")
	original_data = data.copy(deep=True)

	cleaned = drop_missing(dataset, columns=["time", "measurement"])

	assert isinstance(cleaned, Dataset)
	assert cleaned.independent_column == "time"
	assert cleaned.data.index.tolist() == [10, 20]
	assert pd.isna(cleaned.data.loc[10, "note"])
	assert dataset.data.equals(original_data)


def test_drop_missing_raises_when_no_rows_remain():
	"""Reject cleaning when every row has a selected missing value."""
	data = pd.DataFrame({"time": [0.0, 1.0], "measurement": [float("nan"), float("nan")]})
	dataset = Dataset(data, independent_column="time")

	with pytest.raises(ValueError):
		drop_missing(dataset, columns=["time", "measurement"])
