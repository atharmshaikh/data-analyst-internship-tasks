/*
=========================================================
Business Insights – Monthly Performance
Task 06 – Value-Added Analysis

This query highlights top-performing months
and introduces Average Order Value (AOV),
a commonly used business KPI.
=========================================================
*/

SELECT
    EXTRACT(YEAR FROM order_date)  AS order_year,
    EXTRACT(MONTH FROM order_date) AS order_month,
    ROUND(SUM(amount), 2)          AS total_revenue,
    COUNT(DISTINCT order_id)       AS total_orders,
    ROUND(
        SUM(amount) / COUNT(DISTINCT order_id),
        2
    ) AS avg_order_value
FROM orders
GROUP BY
    EXTRACT(YEAR FROM order_date),
    EXTRACT(MONTH FROM order_date)
ORDER BY
    total_revenue DESC
LIMIT 5;

/*
Insights Provided:
- Identifies months with highest revenue
- Compares order volume vs revenue
- Uses AOV to evaluate customer spending behavior
*/