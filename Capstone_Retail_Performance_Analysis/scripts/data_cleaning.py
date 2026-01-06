"""
File: data_cleaning.py

Purpose:
--------
Clean and prepare Superstore sales data for analysis and visualization.

Workflow:
---------
1. Load raw CSV data
2. Standardize column names
3. Parse date columns safely
4. Remove invalid records
5. Create basic time features
6. Export cleaned CSV for Power BI
"""

import pandas as pd
from pathlib import Path


# Paths (relative to repo root)
RAW_DATA_PATH = Path("Capstone_Retail_Performance_Analysis/data/raw/superstore_sales_raw.csv")
OUTPUT_PATH = Path("Capstone_Retail_Performance_Analysis/data/processed/superstore_sales_cleaned.csv")


def main():
    # Load raw data
    df = pd.read_csv(RAW_DATA_PATH, encoding="latin1")

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # Parse date columns safely
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce")

    # Remove rows with missing critical values
    df = df.dropna(subset=["order_id", "order_date", "sales", "quantity"])

    # Ensure numeric columns
    numeric_cols = ["sales", "quantity", "discount", "profit"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Create time-based features
    df["order_year"] = df["order_date"].dt.year  # type: ignore[attr-defined]
    df["order_month"] = df["order_date"].dt.month  # type: ignore[attr-defined]

    # Export cleaned data
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print("Cleaned dataset created at:", OUTPUT_PATH)


if __name__ == "__main__":
    main()
