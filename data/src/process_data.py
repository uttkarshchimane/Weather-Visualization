import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df.dropna(inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    return df