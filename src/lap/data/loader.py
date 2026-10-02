import os
import pandas as pd

class DataLoadError(Exception):
    """Raised when a CSV file cannot be loaded as tabular data."""
    pass

def load_csv(filepath):
    """Load a CSV file into a pandas DataFrame."""
    if os.path.exists(filepath):
        try:
            df = pd.read_csv(filepath)
            return df
        except(pd.errors.EmptyDataError):
            raise DataLoadError()
    else:
        raise FileNotFoundError