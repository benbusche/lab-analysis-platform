import pandas as pd
import numpy as np

class Dataset:
    """
    A wrapper class to store and access a pandas DataFrame.

    Attributes
    ----------
    data : pd.DataFrame
        The data.
    independent_column : str
        The name of the independent column.
    
    Methods
    -------
    __init__(self, data, independent_column=0)
        Initialize the Dataset with the provided data and independent column.
    column(self, name)
        Get the values of a specified column as a numpy array.
    independent(self)
        Get the values of the independent column as a numpy array.
    columns(self)
        Get the names of all columns in the dataset.
    set_independent(self, independent_column)
        Set the independent column by name or index.
    validate(self)
        Validate the dataset for required properties.
    column_is_numeric(self, column)
        Check if a column contains numeric data.
    """
    def __init__(self,data,independent_column=0):
        """Store a DataFrame and validate its independent column."""
        if isinstance(data, pd.DataFrame):
            self.data = data
        else:
            raise TypeError("data must be a pandas DataFrame")
        
        self.set_independent(independent_column)

        self.validate()

    def column(self,name):
        """Return the values of a named column as a NumPy array."""
        return self.data[name].to_numpy()

    def independent(self):
        """Return the values of the selected independent column."""
        return self.data[self.independent_column].to_numpy()

    def columns(self):
        """Return the dataset's column names as a list."""
        return self.data.columns.tolist()

    def set_independent(self,independent_column):
        """Select the independent column by name or zero-based index."""
        if isinstance(independent_column, str):
            if independent_column in self.data.columns:
                self.independent_column = independent_column
            else:
                raise ValueError("Independent column name does not exist.")
        elif isinstance(independent_column,int):
            if self.data.shape[1] > independent_column:
                self.independent_column = self.data.columns[independent_column]
            else:
                raise ValueError("Independent column index does not exist.")
        else:
            raise TypeError("independent_column must be of type int or str.")

    def validate(self):
        """Raise an error when the dataset does not meet its requirements."""
        if self.data.shape[1] < 2:
            raise ValueError("DataFrame must have at least 2 columns")
        if self.data.empty:
            raise ValueError("DataFrame must have at least 1 row")
        if not self.column_is_numeric(self.data[self.independent_column]):
            raise TypeError("Independent column must be numeric")
        if len(self.data.columns) != len(set(self.data.columns)):
            raise ValueError("Column names must be unique")

    def column_is_numeric(self, column):
        """Return whether a pandas column has a numeric dtype."""
        return pd.api.types.is_numeric_dtype(column)
