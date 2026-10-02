from lap.data.dataset import Dataset


def drop_missing(dataset, columns):
	"""Return a Dataset with rows missing values in the selected columns removed."""
	if not isinstance(dataset, Dataset):
		raise TypeError("dataset must be a Dataset")

	cleaned_data = dataset.data.dropna(subset=columns)
	if cleaned_data.empty:
		raise ValueError("No rows remain after dropping missing values")

	return Dataset(cleaned_data, independent_column=dataset.independent_column)
