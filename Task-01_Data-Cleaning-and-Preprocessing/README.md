# Task 01 – Data Cleaning and Preprocessing

## Role
Data Analyst Intern

## Purpose
This task focuses on transforming raw sales data into a clean, consistent, and
analysis-ready dataset. It represents the **first and most critical stage** of a
real-world data analytics workflow.

The output of this task is treated as a **stable data foundation** and is reused
unchanged in all subsequent internship tasks such as exploratory analysis,
SQL queries, and dashboard development.

---

## Dataset

**Source:** Kaggle – Sample Sales Data  
**Link:** https://www.kaggle.com/datasets/kyanyoga/sample-sales-data  

The dataset contains order-level sales transactions including products,
quantities, prices, and customer-related attributes.

**Size:**
- Rows: 2,823  
- Columns: 25 (raw), 26 (after feature engineering)

---

## Project Structure

```

Task-01_Data-Cleaning-and-Preprocessing/
│
├── data/
│   ├── raw/
│   │   └── sales_data_sample.csv
│   └── processed/
│       └── sales_data_cleaned.csv
│
├── notebooks/
│   └── 01_data_cleaning.ipynb
│
├── scripts/
│   └── run_pipeline.py
│
├── src/
│   └── data_cleaning/
│       ├── __init__.py
│       ├── io.py
│       ├── cleaning.py
│       └── features.py
│
├── pyproject.toml
├── requirements.txt
└── README.md

```

---

## Processing Logic

The data cleaning pipeline performs the following steps:

1. Load raw sales data from CSV
2. Inspect dataset shape, missing values, and duplicates
3. Remove duplicate records
4. Handle missing values:
   - Numerical columns → median
   - Categorical columns → `"Unknown"`
5. Standardize text fields (lowercase, trimmed whitespace)
6. Convert `ORDERDATE` to datetime format
7. Create derived analytical feature:
   - `TOTAL_ORDER_VALUE = QUANTITYORDERED × PRICEEACH`
8. Export the cleaned dataset for downstream use

All logic is implemented in reusable Python modules and shared between the
script and notebook to avoid duplication.

---

## Environment & Dependencies

- Python 3.8+
- Pandas
- NumPy
- Jupyter Notebook
- Virtual environment (`venv`)

Dependency versions are isolated using a virtual environment to ensure
reproducibility across systems.

---

## How to Run (Windows, macOS, Linux)

### 1. Clone the repository
```bash
git clone https://github.com/atharmshaikh/data-analyst-internship-tasks.git
cd data-analyst-internship-tasks/Task-01_Data-Cleaning-and-Preprocessing
```

---

### 2. Create and activate a virtual environment

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install -e .
```

---

### 4. Run the data cleaning pipeline

```bash
python scripts/run_pipeline.py
```

**Output:**

```
data/processed/sales_data_cleaned.csv
```

---

### 5. Run the notebook (optional)

```bash
jupyter notebook
```

Open:

```
notebooks/01_data_cleaning.ipynb
```

---

## Output & Usage

The cleaned dataset is:

* Consistent and standardized
* Free of duplicates
* Ready for analysis and visualization

It is used directly in:

* Exploratory Data Analysis (EDA)
* SQL-based reporting
* Business dashboards (Power BI / Tableau)
* Further analytical tasks

---

## Design Decisions

* **src-based layout** for clean imports and scalability
* **Single source of truth** for cleaning logic
* **Script + notebook parity** to ensure reproducibility
* **No manual data edits** outside the pipeline

---

## Notes

* Generated files (`venv/`, `*.egg-info/`) are excluded via `.gitignore`
* This task is considered **final and stable for downstream analysis**
* No further changes are made to Task-01 once downstream tasks begin

---

## Author  

**Athar Shaikh**  
Data Analyst Intern  
Elevate Labs  