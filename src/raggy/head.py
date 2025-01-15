import json

from datasets import Dataset
import pandas as pd




def get_brodsky():
    df = pd.read_csv('brodsky.csv')
    ds = Dataset.from_pandas(df)

    return ds
    