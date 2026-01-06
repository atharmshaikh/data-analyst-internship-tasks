/*
File: 01_data_cleaning.sql

Purpose:
--------
Prepare raw Superstore sales data for analysis by:
- preserving the raw imported table
- standardizing column names
- enforcing correct data types
- removing invalid or incomplete records

Input Table:
------------
raw_superstore_orders
  (Imported directly from CSV without modification)

Output Table:
-------------
cleaned_superstore_orders
  (Cleaned and analysis-ready version of the data)

Notes:
------
- Raw data is NOT modified
- All transformations are reproducible
- This script can be re-run safely
*/

--------------------------------------------------
-- 1. Basic sanity checks on raw data
--------------------------------------------------

-- Total number of rows in raw table
SELECT COUNT(*) AS total_raw_rows
FROM raw_superstore_orders;

-- Preview raw data structure
SELECT *
FROM raw_superstore_orders
LIMIT 5;

--------------------------------------------------
-- 2. Check for missing or invalid values
--------------------------------------------------

SELECT
  SUM(CASE WHEN "Order ID" IS NULL OR "Order ID" = '' THEN 1 ELSE 0 END) AS missing_order_id,
  SUM(CASE WHEN "Order Date" IS NULL OR "Order Date" = '' THEN 1 ELSE 0 END) AS missing_order_date,
  SUM(CASE WHEN "Sales" IS NULL THEN 1 ELSE 0 END) AS missing_sales,
  SUM(CASE WHEN "Quantity" IS NULL THEN 1 ELSE 0 END) AS missing_quantity,
  SUM(CASE WHEN "Profit" IS NULL THEN 1 ELSE 0 END) AS missing_profit
FROM raw_superstore_orders;

--------------------------------------------------
-- 3. Drop cleaned table if it already exists
--------------------------------------------------

DROP TABLE IF EXISTS cleaned_superstore_orders;

--------------------------------------------------
-- 4. Create cleaned table with standardized columns
--------------------------------------------------

CREATE TABLE cleaned_superstore_orders AS
SELECT
  "Row ID"        AS row_id,
  "Order ID"      AS order_id,
  "Order Date"    AS order_date,
  "Ship Date"     AS ship_date,
  "Ship Mode"     AS ship_mode,

  "Customer ID"   AS customer_id,
  "Customer Name" AS customer_name,
  "Segment"       AS segment,

  "Country"       AS country,
  "City"          AS city,
  "State"         AS state,
  "Postal Code"   AS postal_code,
  "Region"        AS region,

  "Product ID"    AS product_id,
  "Category"      AS category,
  "Sub-Category"  AS sub_category,
  "Product Name"  AS product_name,

  CAST("Sales" AS REAL)        AS sales,
  CAST("Quantity" AS INTEGER)  AS quantity,
  CAST("Discount" AS REAL)     AS discount,
  CAST("Profit" AS REAL)       AS profit

FROM raw_superstore_orders
WHERE
  "Order ID" IS NOT NULL
  AND "Sales" IS NOT NULL
  AND "Quantity" IS NOT NULL;

--------------------------------------------------
-- 5. Validate cleaned data
--