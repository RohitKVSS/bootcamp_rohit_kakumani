import pandas as pd

def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns summary statistics for numeric columns in the DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame
    
    Returns
    -------
    pd.DataFrame
        Summary statistics (count, mean, std, min, quartiles, max)
    """
    return df.describe()