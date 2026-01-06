"""
File: data_validation_and_summary.py

Purpose:
--------
Validate the cleaned Superstore dataset and generate
basic summary tables for reporting and visualization.

Input:
------
data/processed/superstore_sales_cleaned.csv

Outputs:
--------
- summary_overall.csv
- summary_by_region.csv
- summary_by_category.csv
- summary_by_month.csv
"""

import pandas as pd
from pathlib import Path


CLEAN_DATA_PATH = Path(
    "Capstone_Retail_Performance_Analysis/data/processed/superstore_sales_cleaned.csv"
)

OUTPUT_DIR = Path(
    "Capstone_Retail_Performance_Analysis/data/processed/summaries"
)


def main():
    df = pd.read_csv(CLEAN_DATA_PATH, parse_dates=["order_date", "ship_date"])

    # Basic validation
    print("Rows:", len(df))
    print("Missing values:")
    print(df.isnull().sum())

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Overall summary
    overall = pd.DataFrame({
        "total_sales": [df["sales"].sum()],
        "total_profit": [df["profit"].sum()],
        "total_orders": [df["order_id"].nunique()],
        "total_quantity": [df["quantity"].sum()]
    })
    overall.to_csv(OUTPUT_DIR / "summary_overall.csv", index=False)

    # By region
    by_region = (
        df.groupby("region", as_index=False)
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            total_quantity=("quantity", "sum")
        )
    )
    by_region.to_csv(OUTPUT_DIR / "summary_by_region.csv", index=False)

    # By category
    by_category = (
        df.groupby("category", as_index=False)
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            total_quantity=("quantity", "sum")
        )
    )
    by_category.to_csv(OUTPUT_DIR / "summary_by_category.csv", index=False)

    # By month
    by_month = (
        df.groupby(["order_year", "order_month"], as_index=False)
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            total_quantity=("quantity", "sum")
        )
        .sort_values(["order_year", "order_month"])
    )
    by_month.to_csv(OUTPUT_DIR / "summary_by_month.csv", index=False)

    print("Summary CSVs created in:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
