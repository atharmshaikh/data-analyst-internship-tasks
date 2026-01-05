# Methodology

## Aggregation Strategy
Monthly aggregation was chosen to identify time-based sales trends
and potential seasonality patterns.

## Metrics Used
- **Monthly Revenue**: SUM(amount)
- **Order Volume**: COUNT(DISTINCT order_id)
- **Average Order Value (AOV)**: Revenue ÷ Order Volume

## Grouping Logic
Data is grouped by both year and month to prevent combining
records from the same month across different years.

## Analysis Focus
The analysis focuses on understanding:
- Revenue growth or decline over time
- Changes in customer purchasing frequency
- High-performing months based on revenue