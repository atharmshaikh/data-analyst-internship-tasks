-- Reusable aggregation queries

-- Monthly revenue trend
SELECT
    substr(o.order_purchase_timestamp, 1, 7) AS month,
    SUM(p.payment_value) AS monthly_revenue
FROM orders o
JOIN order_payments p ON o.order_id = p.order_id
GROUP BY month
ORDER BY month;

-- Orders count by state
SELECT
    c.customer_state,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_state
ORDER BY total_orders DESC;
