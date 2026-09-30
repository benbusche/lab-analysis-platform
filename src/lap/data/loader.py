import os
import pandas as pd

class DataLoadError(Exception):
    pass

def load_csv(filepath):
    if os.path.exists(filepath):
        try:
            df = pd.read_csv(filepath)
            return df
        except(pd.errors.EmptyDataError):
            raise DataLoadError()
    else:
        raise FileNotFoundError