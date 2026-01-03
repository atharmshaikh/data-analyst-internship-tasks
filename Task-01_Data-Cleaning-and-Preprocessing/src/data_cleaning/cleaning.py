import pandas as pd


def inspect(df: pd.DataFrame) -> None:
    """
    Print basic dataset diagnostics.
    """
    print("Dataset shape:", df.shape)
    print("\nMissing values per column:\n", df.isna().sum())
    print("\nDuplicate rows:", df.duplicated().sum())


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw sales data.

    Steps:
    - Remove duplicates
    - Handle missing values
    - Standardize text columns
    - Convert ORDERDATE to datetime
    """
    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Handle missing values
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].fillna("Unknown")
        else:
            df[column] = df[column].fillna(df[column].median())

    # Standardize text columns
    text_columns = df.select_dtypes(include="object").columns
    for column in text_columns:
        df[column] = df[column].str.strip().str.lower()

    # Convert ORDERDATE to datetime
    if "ORDERDATE" in df.columns:
        df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")

    return df
