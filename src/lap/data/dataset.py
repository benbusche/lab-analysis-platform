import pandas as pd
import numpy as np

class Dataset:
    def __init__(self,data,independent_column=0):
        if isinstance(data, pd.DataFrame):
            self.data = data
        else:
            raise TypeError("data must be a pandas DataFrame")
        
        self.set_independent(independent_column)
        

    #RETURNING FUNCTIONS
    def column(self,name):
        return self.data[name].to_numpy()

    def independent(self):
        return self.data[self.independent_column].to_numpy()

    def columns(self):
        return self.data.columns.tolist()

    #EDITING FUNCTIONS
    def set_independent(self,independent_column):
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