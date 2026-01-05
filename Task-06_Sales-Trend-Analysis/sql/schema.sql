/*
=========================================================
Schema: Orders Table
Task 06 – Sales Trend Analysis Using Aggregations

This schema represents a simplified online sales dataset
used for time-based revenue and order volume analysis.

Compatible with:
- PostgreSQL
- MySQL
- SQLite
=========================================================
*/

CREATE TABLE IF NOT EXISTS orders (
    order_id    TEXT PRIMARY KEY,
    order_date  DATE NOT NULL,
    product_id  TEXT NOT NULL,
    amount      NUMERIC(10, 2) NOT NULL
);

/*
Notes:
- order_id is assumed to be unique per order
- amount represents total revenue per order
- order_date is used for monthly trend analysis
*/