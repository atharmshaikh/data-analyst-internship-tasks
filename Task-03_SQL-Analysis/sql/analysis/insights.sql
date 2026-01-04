-- Business-focused SQL analysis for Task 03

-- 1. Revenue by customer state
SELECT
    c.customer_state,
    ROUND(SUM(p.payment_value), 2) AS total_revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_payments p ON o.order_id = p.order_id
GROUP BY c.customer_state
ORDER BY total_revenue DESC;

-- 2. Average order value (AOV)
SELECT
    ROUND(AVG(order_total), 2) AS avg_order_value
FROM (
    SELECT
        o.order_id,
        SUM(p.payment_value) AS order_total
    FROM orders o
    JOIN order_payments p ON o.order_id = p.order_id
    GROUP BY o.order_id
);

-- 3. Monthly revenue trend
SELECT
    substr(o.order_purchase_timestamp, 1, 7) AS month,
    ROUND(SUM(p.payment_value), 2) AS monthly_revenue
FROM orders o
JOIN order_payments p ON o.order_id = p.order_id
GROUP BY month
ORDER BY month;

-- 4. Top customers by total spend
SELECT
    c.customer_id,
    ROUND(SUM(p.payment_value), 2) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_payments p ON o.order_id = p.order_id
GROUP BY c.customer_id
ORDER BY total_spent DESC
LIMIT 10;
