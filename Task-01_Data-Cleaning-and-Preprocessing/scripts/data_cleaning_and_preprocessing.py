"""
Task 01: Data Cleaning and Preprocessing

Author: Athar Shaikh
Role: Data Analyst Intern

Description:
This script cleans raw sales data and prepares it for analysis by:
- Handling missing values
- Removing duplicates
- Standardizing text
- Converting date columns
- Creating derived features
"""

import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load CSV file into a DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError("Input file not found. Check the file path.")


def inspect_data(df: pd.DataFrame) -> None:
    """
    Print basic dataset information.
    """
    print("\nDataset Shape:", df.shape)
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nDuplicate Rows:", df.duplicated().sum())


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform data cleaning steps.
    """

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna("Unknown")
        else:
            df[col] = df[col].fillna(df[col].median())

    # Standardize text columns
    text_cols = df.select_dtypes(include="object").columns
    for col in text_cols:
        df[col] = df[col].str.strip().str.lower()

    # Convert date column if exists
    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    return df


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create new derived features.
    """

    if {"quantity", "price"}.issubset(df.columns):
        df["total_order_value"] = df["quantity"] * df["price"]

    return df


def save_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Save cleaned dataset to CSV.
    """
    df.to_csv(output_path, index=False)


def main():
    """
    Execute the full data cleaning pipeline.
    """

    input_path = "../data/sales_data_sample.csv"
    output_path = "../data/sales_data_cleaned.csv"

    df = load_data(input_path)
    inspect_data(df)

    df = clean_data(df)
    df = feature_engineering(df)

    save_data(df, output_path)

    print("\nData cleaning completed successfully.")


if __name__ == "__main__":
    main()
