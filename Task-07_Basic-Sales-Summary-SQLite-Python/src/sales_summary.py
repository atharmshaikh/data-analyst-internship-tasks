"""
Task 07: Basic Sales Summary using SQLite & Python

Description:
Connects to a SQLite database, aggregates product-level sales data,
and visualizes revenue using a simple bar chart.

Author: Athar Shaikh
"""

import sqlite3
import logging
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# -------------------------------------------------------------------
# Logging Configuration
# -------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# -------------------------------------------------------------------
# Path Resolution
# -------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "data" / "sales_data.db"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


# -------------------------------------------------------------------
# Data Access Layer
# -------------------------------------------------------------------
def fetch_sales_summary() -> pd.DataFrame:
    """
    Fetch aggregated sales summary from SQLite database.

    Returns:
        pd.DataFrame: Product-wise total quantity and revenue
    """
    if not DB_PATH.exists():
        raise FileNotFoundError(f"Database not found at: {DB_PATH}")

    query = """
        SELECT
            product,
            SUM(quantity) AS total_qty,
            SUM(quantity * price) AS revenue
        FROM sales
        GROUP BY product
        ORDER BY revenue DESC;
    """

    logging.info("Connecting to SQLite database")

    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query(query, conn)

    if df.empty:
        logging.warning("No data returned from sales table")

    return df


# -------------------------------------------------------------------
# Visualization Layer
# -------------------------------------------------------------------
def plot_revenue(df: pd.DataFrame) -> None:
    """
    Plot revenue by product and save the chart.

    Args:
        df (pd.DataFrame): Aggregated sales data
    """
    if df.empty:
        logging.warning("Skipping plot generation due to empty DataFrame")
        return

    logging.info("Generating revenue bar chart")

    ax = df.plot(
        kind="bar",
        x="product",
        y="revenue",
        legend=False,
        title="Revenue by Product",
    )

    ax.set_xlabel("Product")
    ax.set_ylabel("Revenue")
    plt.xticks(rotation=30)

    output_path = OUTPUT_DIR / "sales_chart.png"
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    logging.info("Chart saved to %s", output_path)


# -------------------------------------------------------------------
# Application Entry Point
# -------------------------------------------------------------------
def main() -> None:
    """Main execution workflow."""
    try:
        df = fetch_sales_summary()
        print(df)
        plot_revenue(df)
    except Exception as exc:
        logging.error("Task execution failed: %s", exc)
        raise


if __name__ == "__main__":
    main()