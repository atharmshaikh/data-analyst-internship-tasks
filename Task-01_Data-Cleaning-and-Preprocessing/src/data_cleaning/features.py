import pandas as pd


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create derived features for analysis.

    Feature created:
    - TOTAL_ORDER_VALUE = QUANTITYORDERED * PRICEEACH
    """
    df = df.copy()

    required_columns = {"QUANTITYORDERED", "PRICEEACH"}
    if required_columns.issubset(df.columns):
        df["TOTAL_ORDER_VALUE"] = (
            df["QUANTITYORDERED"] * df["PRICEEACH"]
        )

    return df
