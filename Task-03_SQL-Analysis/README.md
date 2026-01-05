# Task 03 : SQL for Data Analysis

**End-to-End SQL Analytics Using SQLite**

<p align="center">
  <a href="https://www.sqlite.org/index.html">
    <img src="https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
  </a>
  <a href="https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce">
    <img src="https://img.shields.io/badge/Dataset-Olist_E--Commerce-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white">
  </a>

</p>

---

## Overview

This repository contains **Task-03: SQL for Data Analysis**, completed using a **real-world e-commerce dataset** and an **industry-aligned SQL workflow**.

The goal of this task is **not just writing SQL queries**, but demonstrating the full analytical process:

* Designing an analytical schema
* Ingesting raw data safely
* Validating data integrity
* Performing business-focused SQL analysis
* Producing reproducible, verifiable results

The analysis is implemented using **SQLite**, a lightweight and widely used database for analytics, prototyping, and interviews.

---

## Dataset

**Name:** Brazilian E-Commerce Public Dataset by Olist
**Source:** Kaggle
**Link:**
[https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

**Description:**
The dataset contains real transactional data from a Brazilian e-commerce platform, including customers, orders, payments, timestamps, and geographic information.

> Raw CSV files are intentionally **not committed** to this repository.
> Only the processed analytical database is version-controlled.

---

## Tools & Technologies

| Category          | Tool                  |
| ----------------- | --------------------- |
| Database          | SQLite                |
| SQL Client        | DB Browser for SQLite |
| Operating Systems | Windows, Linux, macOS |
| Version Control   | Git & GitHub          |

---

## Project Structure

```text
Task-03_SQL-Analysis/
├── data/
│   ├── analytics/
│   │   └── olist_analytics.db
│   ├── processed/
│   │   └── README.md
│   ├── raw/
│   │   └── README.md
│   └── README.md
├── reports/
│   ├── screenshots/
│   │   ├── avg_order_value.png
│   │   ├── monthly_revenue.png
│   │   └── revenue_by_state.png
│   └── README.md
├── sql/
│   ├── analysis/
│   │   └── insights.sql
│   ├── queries/
│   │   └── aggregations.sql
│   └── schema/
│       └── schema.sql
└── README.md
```

---

## Workflow Summary

The following **industry-standard workflow** was followed:

### 1. Raw Data Handling

* Dataset downloaded locally from Kaggle
* Raw CSV files kept **outside GitHub**
* Prevents large files, duplication, and licensing issues

### 2. Analytical Database Preparation

* A SQLite database file was created to ingest raw CSV data
* Schema definitions and analytical SQL queries were executed
* The database file was saved in its final form after all queries and validations were completed

* Final database available at: `data/analytics/olist_analytics.db`

### 3. Schema Design

Final analytical tables:

* `customers`
* `orders`
* `order_payments`

Schema definition is available in:

```
sql/schema/schema.sql
```

### 4. Data Ingestion (Staging Pattern)

Instead of direct imports, a **staging approach** was used:

```
CSV → *_raw tables → final tables
```

This ensures:

* Controlled column selection
* Easier debugging
* Correct referential integrity

### 5. Data Validation

* Row count verification
* Join validation between tables
* Debugging mismatched imports
* Ensured valid relationships:

  * customers ↔ orders
  * orders ↔ order_payments

### 6. SQL Analysis

Business-focused SQL queries were written to answer real analytical questions.

All analysis queries are available in:

```
sql/analysis/insights.sql
```

---

## Analysis & Results

### Revenue by State

Identifies top revenue-contributing geographic regions.



![Revenue by State](reports/screenshots/revenue_by_state.png)

---

### Average Order Value (AOV)

Measures the average revenue generated per order.


![Average Order Value](reports/screenshots/avg_order_value.png)

---

### Monthly Revenue Trend

Shows revenue aggregated by month to analyze growth and seasonality.

![Monthly Revenue Trend](reports/screenshots/monthly_revenue.png)

---

## How to Explore This Analysis
### Prerequisites (All Platforms)

* SQLite
* DB Browser for SQLite

---

### Windows

#### One-time: Analytical Database Creation (Manual)

1. Download the dataset from Kaggle
   Brazilian E-Commerce Public Dataset by Olist
2. Extract the CSV files locally
3. Download and install **DB Browser for SQLite**
   [https://sqlitebrowser.org/dl/](https://sqlitebrowser.org/dl/)
4. Open **DB Browser for SQLite**
5. Create a new database file
6. Import the CSV files into SQLite as staging tables
7. Execute schema and analytical SQL queries
8. Save the final database as:

```
data/analytics/olist_analytics.db
```

Only the final analytical database is committed to this repository.

#### Exploring the Analysis

1. Open **DB Browser for SQLite**
2. Open the database file:

```
data/analytics/olist_analytics.db
```

3. Run analytical queries from:

```
sql/analysis/insights.sql
```

4. Validate results using screenshots in:

```
reports/screenshots/
```

---

### Linux (Ubuntu / Mint / Debian)

#### Installation

```bash
sudo apt update
sudo apt install sqlitebrowser
```

#### One-time: Analytical Database Creation (Manual)

1. Download and extract the Kaggle dataset locally
2. Open **DB Browser for SQLite**
3. Create a new SQLite database file
4. Import CSV files into staging tables
5. Execute schema and analysis SQL scripts
6. Save the final database as:

```
data/analytics/olist_analytics.db
```

#### Exploring the Analysis

1. Open **DB Browser for SQLite**
2. Load the database file:

```
data/analytics/olist_analytics.db
```

3. Execute queries from:

```
sql/analysis/insights.sql
```

4. Cross-check outputs with screenshots in `reports/screenshots/`

---

### macOS

#### Installation

```bash
brew install --cask db-browser-for-sqlite
```

#### One-time: Analytical Database Creation (Manual)

1. Download and extract the Kaggle CSV files
2. Open **DB Browser for SQLite**
3. Create a new SQLite database
4. Import CSV files into staging tables
5. Run schema and analytical SQL queries
6. Save the final database as:

```
data/analytics/olist_analytics.db
```

#### Exploring the Analysis

1. Open **DB Browser for SQLite**
2. Open the database file:

```
data/analytics/olist_analytics.db
```

3. Run queries from:

```
sql/analysis/insights.sql
```

4. Compare results with screenshots in `reports/screenshots/`

---

## Reproducibility

* Raw data can be re-downloaded from the Kaggle source
* Database schema and analytical SQL queries are fully version-controlled
* Screenshots provide proof of query execution and results
* The analytical database can be manually recreated using external raw data

---

## Key Takeaways

This project demonstrates:

* Practical SQL for data analytics
* Real-world dataset handling
* Manual data ingestion and validation using SQLite
* Clear separation of raw data, analytical outputs, and reports
* Industry-aligned documentation

---

## Author

**Athar Shaikh**  
Data Analyst Intern  
Elevate Labs  