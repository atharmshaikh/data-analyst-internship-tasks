# Task 01 – Data Cleaning and Preprocessing

## Overview
This project focuses on cleaning and preprocessing raw sales data to make it suitable for analysis, SQL querying, and dashboard development.  
It was completed as part of a **Data Analyst Internship** and follows a clean, modular, and reproducible workflow.

Data cleaning is a critical first step in any real-world analytics pipeline, and this task simulates that responsibility using Python and Pandas.

---

## Objective
- Clean raw sales data
- Handle missing values and duplicate records
- Standardize text and data types
- Create basic derived features
- Export a clean dataset for downstream tasks

---

## Tools & Technologies
- Python 3
- Pandas
- NumPy
- Jupyter Notebook
- VS Code

---

## Dataset Source

[![Kaggle Dataset](https://img.shields.io/badge/Dataset-Kaggle-blue?logo=kaggle)](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)

The dataset contains order-level sales information including products, quantities, prices, and dates.

---

## Project Structure
```

Task-01_Data-Cleaning-and-Preprocessing/
├── data/
│   ├── sales_data_sample.csv        # Raw dataset
│   └── sales_data_cleaned.csv       # Cleaned dataset
├── notebooks/
│   └── data_cleaning.ipynb          # Step-by-step explanation
├── scripts/
│   └── data_cleaning_and_preprocessing.py  # Reusable cleaning pipeline
├── README.md
├── requirements.txt
└── .gitignore

```

---

## Dataset Description
- **sales_data_sample.csv**  
  Contains raw sales records including product details, quantities, prices, and order-related information.

- **sales_data_cleaned.csv**  
  Cleaned and standardized version of the dataset, ready for analysis and visualization.

---

## Steps Performed
1. Loaded raw data using Pandas
2. Performed initial inspection (shape, missing values, duplicates)
3. Removed duplicate records
4. Handled missing values:
   - Numerical columns → median
   - Categorical columns → placeholder values
5. Standardized text columns (lowercase, trimmed spaces)
6. Converted date columns to datetime format
7. Created a derived feature: `total_order_value`
8. Saved the cleaned dataset for reuse

---

## How to Run the Project

### 1. Navigate to the project folder
```bash
cd Task-01_Data-Cleaning-and-Preprocessing
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the cleaning script

```bash
cd scripts
python data_cleaning_and_preprocessing.py
```

### 5. (Optional) Run the notebook

```bash
cd ..
jupyter notebook
```

Open `notebooks/data_cleaning.ipynb`

---

## Outcome

* A clean and structured dataset ready for:

  * Exploratory Data Analysis (EDA)
  * SQL-based analysis
  * Power BI dashboards
* The cleaned dataset is reused in subsequent internship tasks.

---

## Reusability

This task serves as the **data foundation** for later internship work, including:

* Exploratory Data Analysis
* Sales Trend Analysis
* Interactive Dashboards

---

## Notes

* A Python virtual environment is used to ensure dependency isolation.
* The `venv/` directory is excluded from version control via `.gitignore`.

---

## Author

**Athar Shaikh**  
Data Analyst Intern  
Elevate Labs  