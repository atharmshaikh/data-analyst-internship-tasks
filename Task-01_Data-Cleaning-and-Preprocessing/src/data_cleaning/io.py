from pathlib import Path
import pandas as pd


def load_csv(path: Path) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Parameters
    ----------
    path : Path
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
    """
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    return pd.read_csv(path)


def save_csv(df: pd.DataFrame, path: Path) -> None:
    """
    Save DataFrame to CSV.

    Parameters
    ----------
    df : pd.DataFrame
    path : Path
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
