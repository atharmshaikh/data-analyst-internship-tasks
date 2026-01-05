# Analysis Reports

This directory contains the **reporting artifacts** generated from SQL-based
data analysis performed for **Task-03: SQL for Data Analysis**.

The purpose of this directory is to **present, validate, and communicate**
analytical results derived from the final SQLite database.

---

## Data Source

All reports in this directory are generated from the **final analytical SQLite database**:

```
data/analytics/olist_analytics.db
```

This database represents the **output of the analytical workflow** and is not raw input data.

---

## Report Contents

### Screenshots

The `screenshots/` directory contains visual snapshots of query results captured
directly from **DB Browser for SQLite** after executing analytical SQL queries.

Included analyses:

* **Revenue by State**
  Geographic distribution of total revenue across states.

* **Average Order Value (AOV)**
  Average revenue generated per order.

* **Monthly Revenue Trend**
  Time-series analysis of revenue aggregated by month.

These screenshots act as **evidence of query execution and correctness**.

---

## Reporting Workflow

The reporting process followed these steps:

1. Execute analytical SQL queries on the final SQLite database
2. Validate query outputs against expected business logic
3. Review results using DB Browser for SQLite
4. Capture result snapshots for documentation and verification
5. Store screenshots as lightweight reporting artifacts

No CSV exports were generated, as the goal is **result verification**, not data redistribution.

---

## Traceability

* All SQL queries used to generate these reports are available at:

```
sql/analysis/insights.sql
```

* Database schema definitions are available at:

```
sql/schema/schema.sql
```

This ensures full **traceability from schema → query → result → report**.

---

## Notes

* Screenshots are used instead of exported datasets to keep the repository lightweight
* Reports are designed for **review and validation**, not downstream consumption
* The database and SQL queries together serve as the authoritative analytical source

---

### Summary

This reporting structure ensures that:

* Analytical results are reproducible using the documented schema and queries
* Outputs are verifiable without rebuilding the database
* Documentation clearly separates analysis logic from presentation
