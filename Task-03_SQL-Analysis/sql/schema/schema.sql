-- Database schema for Task 03: SQL for Data Analysis
-- This schema defines the final analytical tables

CREATE TABLE customers (
    customer_id TEXT PRIMARY KEY,
    customer_city TEXT,
    customer_state TEXT
);

CREATE TABLE orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT,
    order_purchase_timestamp TEXT
);

CREATE TABLE order_payments (
    order_id TEXT,
    payment_value REAL
);
