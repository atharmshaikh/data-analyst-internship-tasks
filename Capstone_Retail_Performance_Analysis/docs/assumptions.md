# Assumptions

This document lists the key assumptions made during the analysis.
These assumptions help define the scope and interpretation of results.

---

## 1. Data Accuracy

It is assumed that:

- Sales, profit, and quantity values in the dataset are accurate
- No duplicate transactions exist beyond what is present in the source
- Dates represent actual order and shipment timelines

The analysis does not attempt to correct or infer missing business context.

---

## 2. Pricing & Profit Logic

- The `profit` column is assumed to already reflect:
  - cost
  - discounts
  - pricing logic
- No recalculation of profit margins is performed
- Discounts are treated as final values, not adjustable parameters

---

## 3. Time-Based Analysis

- Monthly trends are based on `order_date`, not `ship_date`
- Partial months are included without adjustment
- Seasonal effects are observed descriptively, not statistically tested

---

## 4. Regional & Category Definitions

- Region and category labels are assumed to be consistent
- No reclassification or grouping is applied
- Categories are treated at a high level only

Sub-category analysis is intentionally excluded to keep visuals focused.

---

## 5. Dashboard Usage

- The dashboard is assumed to be used for **exploratory review**
- It is not designed for forecasting or predictive decisions
- Users are expected to interpret results with business context

---

## Summary

These assumptions define the boundaries of the analysis.
Results should be interpreted within this scope and not treated
as definitive business conclusions.