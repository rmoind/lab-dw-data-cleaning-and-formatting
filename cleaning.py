import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def drop_nulls_duplicates(df):
    return df.dropna().drop_duplicates()