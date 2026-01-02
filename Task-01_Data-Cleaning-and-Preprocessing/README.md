# Task 1: Data Cleaning and Preprocessing


---

## 📁 Dataset Used

**Dataset Name:** Sales Data  
**Source:** [Sales Data Sample on Kaggle](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)

The dataset contains order information including product details, customer information, dates, sales values, and other metadata.

---

## 🛠 Tools & Environment

- **Programming Language:** Python 3.13  
- **IDE:** Visual Studio Code  
- **Libraries Used:**  
  - `pandas`


---

##  Cleaning Steps Performed

1. **Loaded dataset** using `pandas.read_csv()` with appropriate encoding (`ISO-8859-1`).
2. **Handled missing values**:
   - Filled missing address-related fields with empty strings or default values.
   - Filled numeric columns with median values.
3. **Standardized text values** by:
   - Lowercasing
   - Stripping whitespaces
   - Removing hidden characters (tabs, newlines)
4. **Converted dates** to `datetime` format (`ORDERDATE`) and dropped rows with invalid dates.
5. **Renamed columns** to be lowercase and use underscores instead of spaces.
6. **Converted data types** for relevant numeric columns using `pd.to_numeric()`.
7. **Created new column** `total_order_value` by multiplying `quantityordered` × `priceeach`.
8. **Removed duplicate records** using `drop_duplicates()`.
9. **Saved the cleaned dataset** as `sales_data_cleaned.csv`.

---

## 📂 Files Included

- `sales_data_sample.csv` – Original raw dataset  
- `sales_data_cleaned.csv` – Final cleaned dataset  
- `README.md` – This file

---

