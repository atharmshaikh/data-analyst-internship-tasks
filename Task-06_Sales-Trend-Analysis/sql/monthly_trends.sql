/*
=========================================================
Monthly Sales Trend Analysis
Task 06 – Core Aggregation Logic

Objective:
- Calculate monthly revenue
- Calculate monthly order volume
- Group data by year and month to avoid cross-year mixing
=========================================================
*/

SELECT
    EXTRACT(YEAR FROM order_date)  AS order_year,
    EXTRACT(MONTH FROM order_date) AS order_month,
    SUM(amount)                    AS monthly_revenue,
    COUNT(DISTINCT order_id)       AS order_volume
FROM orders
GROUP BY
    EXTRACT(YEAR FROM order_date),
    EXTRACT(MONTH FROM order_date)
ORDER BY
    order_year,
    order_month;

/*
Why this approach:
- EXTRACT(YEAR, MONTH) ensures correct time granularity
- SUM(amount) measures total revenue
- COUNT(DISTINCT order_id) avoids duplicate order counts
- ORDER BY provides deterministic, readable output
*/