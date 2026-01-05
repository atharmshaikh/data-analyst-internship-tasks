# Data Directory

This directory contains **data-related artifacts** for Task-03, clearly
separating raw inputs from analytical outputs.

## Structure

- `raw/`  
  Placeholder for original CSV files downloaded from Kaggle.  
  Raw datasets are **intentionally not committed** to this repository.

- `processed/`  
  Notes and documentation related to data validation, transformations,
  and intermediate processing decisions.

- `analytics/`  
  Contains the **final analytical SQLite database** used for SQL analysis.

  - `olist_analytics.db` → Output of the completed analytical workflow

## Workflow Followed

```

Raw CSV files
↓
SQLite staging tables
↓
Final analytical tables
↓
Business-focused SQL analysis

```

**Note.** :  The SQLite database provided here is a **reference analytical artifact**.
It is not raw data and not part of a live ETL pipeline.

