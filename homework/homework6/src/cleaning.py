import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def fill_missing_median(df: pd.DataFrame, columns=None) -> pd.DataFrame:
    """
    Fill missing values in specified columns (or all numeric columns) with the median.
    """
    df = df.copy()
    if columns is None:
        columns = df.select_dtypes(include="number").columns
    for col in columns:
        median_val = df[col].median()
        df[col].fillna(median_val, inplace=True)
    return df


def drop_missing(df: pd.DataFrame, columns=None) -> pd.DataFrame:
    """
    Drop rows with missing values. If columns specified, drop if NA in those columns only.
    """
    df = df.copy()
    if columns is None:
        return df.dropna()
    else:
        return df.dropna(subset=columns)


def normalize_data(df: pd.DataFrame, columns=None) -> pd.DataFrame:
    """
    Normalize numeric columns to range [0,1] using MinMax scaling.
    """
    df = df.copy()
    if columns is None:
        columns = df.select_dtypes(include="number").columns

    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df
