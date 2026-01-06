# Methodology

This document describes the step-by-step approach followed in the
Retail Performance Analysis capstone project.

The methodology focuses on clarity, correctness, and reproducibility,
rather than automation or advanced modeling.

---

## 1. Data Ingestion

The project begins with a raw transactional retail dataset
(Superstore Sales Dataset).

- The raw dataset is stored in `data/raw/`
- The file is treated as **read-only**
- No manual edits are performed on the raw data

This ensures that the original data state is always preserved
and can be reprocessed if needed.

---

## 2. Data Cleaning

Data cleaning is performed using a Python script
(`scripts/data_cleaning.py`).

Key steps include:

- Standardizing column names
  - lowercase
  - underscores instead of spaces
- Parsing date columns (`order_date`, `ship_date`)
- Converting numeric fields (`sales`, `profit`, `quantity`, `discount`)
- Removing rows with missing critical values
- Creating basic time features:
  - `order_year`
  - `order_month`

The output of this step is a clean, analysis-ready dataset saved as:

```
data/processed/superstore_sales_cleaned.csv
```

---

## 3. Data Validation

After cleaning, the dataset is validated to ensure:

- No unexpected null values in key fields
- Reasonable row counts
- Consistent data types

Validation results are printed during script execution
and reviewed manually.

This step helps catch data issues early before visualization.

---

## 4. Aggregation & Summaries

A second Python script
(`scripts/data_validation_and_summary.py`)
is used to generate summary tables.

The following summaries are created:

- Overall metrics (sales, profit, orders, quantity)
- Sales and profit by region
- Sales and profit by category
- Monthly sales and profit trends

These summaries are stored as CSV files under:

```
data/processed/summaries/
```

The summaries simplify dashboard creation and improve performance.

---

## 5. Dashboard Development

The cleaned dataset and summary tables are loaded into Power BI.

The dashboard is designed with three pages:

1. **Overview** — high-level KPIs and trends
2. **Regional Performance** — region-wise comparison
3. **Category Performance** — category-level comparison

Slicers are used to enable interactive filtering across pages.

---

## 6. Output & Documentation

Final outputs include:

- Power BI dashboard file (`.pbix`)
- Dashboard screenshots for preview
- Cleaned datasets and summaries
- Written documentation explaining assumptions and limitations

This ensures the project can be reviewed without running code.

---

## Summary

This methodology emphasizes:

- Clear separation of raw and processed data
- Script-based transformations
- Simple, explainable logic
- Visual outputs designed for decision review

The approach prioritizes understanding and correctness
over complexity.