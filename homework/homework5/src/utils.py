import os
import pandas as pd

def write_df(df: pd.DataFrame, path: str, index: bool = False) -> None:
    """Write DataFrame to CSV or Parquet based on file suffix."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    suffix = os.path.splitext(path)[1].lower()
    
    try:
        if suffix == ".csv":
            df.to_csv(path, index=index)
        elif suffix == ".parquet":
            try:
                df.to_parquet(path, index=index)
            except ImportError:
                raise ImportError("Parquet engine not found. Install 'pyarrow' or 'fastparquet'.")
        else:
            raise ValueError(f"Unsupported file type: {suffix}")
        print(f"✅ Saved DataFrame to {path}")
    except Exception as e:
        print(f"❌ Failed to write DataFrame to {path}: {e}")


def read_df(path: str) -> pd.DataFrame:
    """Read DataFrame from CSV or Parquet based on file suffix."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    
    suffix = os.path.splitext(path)[1].lower()
    
    try:
        if suffix == ".csv":
            df = pd.read_csv(path, parse_dates=True)
        elif suffix == ".parquet":
            try:
                df = pd.read_parquet(path)
            except ImportError:
                raise ImportError("Parquet engine not found. Install 'pyarrow' or 'fastparquet'.")
        else:
            raise ValueError(f"Unsupported file type: {suffix}")
        
        print(f"✅ Loaded DataFrame from {path} (shape={df.shape})")
        return df
    except Exception as e:
        print(f"❌ Failed to read DataFrame from {path}: {e}")
        raise
