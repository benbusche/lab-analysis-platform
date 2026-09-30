import pandas as pd
import numpy as np

class Dataset:
    def __init__(self,data):
        if isinstance(data, pd.DataFrame):
            self.data = data
        else:
            raise(TypeError)

    def column(self,name):
        return self.data[name].to_numpy()

    def columns(self):
        return self.data.columns.tolist()
