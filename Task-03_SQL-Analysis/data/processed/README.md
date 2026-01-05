# Processed Data

This folder represents processed and analysis-ready state of data.

For Task-03, the processed output is a SQLite database:
- `data/analytics/olist_analytics.db`

The database was created by:
1. Importing raw CSV files into staging tables
2. Inserting cleaned data into final analytical tables
3. Verifying referential integrity and row counts

No additional processed files are stored separately, as the SQLite database
serves as the final analytical output.
