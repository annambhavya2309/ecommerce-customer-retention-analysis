# E-Commerce Customer Retention Analysis

## Project Overview
This project analyzes online retail transaction data to understand customer purchasing behavior, identify repeat customers, examine purchase recency, and identify high-value customers.

## Objectives
- Inspect and clean retail transaction data.
- Analyze repeat and one-time customers.
- Group customers by time since their last purchase.
- Identify the top 10 customers by total spending.
- Generate insights that can help improve customer retention.

## Tools and Technologies
- Python
- Pandas
- Excel
- PivotTables and Charts
- CSV Dataset

## Dataset
The project uses the Online Retail dataset, which contains transaction records from December 2010 to December 2011.

Original dataset: https://archive.ics.uci.edu/dataset/352/online+retail

## Data Cleaning
- Inspected missing values and duplicate records.
- Removed duplicate transactions.
- Examined cancellation transactions and negative quantities.
- Prepared a cleaned dataset for customer purchase analysis.

## Key Findings
- Original records: 541,909
- Duplicate rows removed: 5,268
- Cleaned transaction rows: 536,641
- Customer records used for sales analysis: 392,692
- Unique customers in the summary: 4,338
- Total sales value: £8,887,208.89
- Repeat customers: 2,845 (65.58%)
- One-time customers: 1,493 (34.42%)

## Customer Recency Analysis
Customers were grouped by the number of days since their last recorded purchase:

- 0–30 days: 1,667 customers
- 31–90 days: 1,222 customers
- 91–180 days: 591 customers
- 180+ days: 858 customers

## Top Customer Finding
The highest-spending customer in the analysis was Customer ID 14646, with approximately £280,206 in recorded spending.

## Visualizations
The Excel workbook contains charts for:
- Repeat vs One-Time Customers
- Customers by Last Purchase Recency
- Top 10 Customers by Spending

## Business Insights
- Repeat customers account for approximately 65.58% of customers in the summary.
- Customers with longer gaps since their last purchase could be considered for re-engagement campaigns.
- High-spending customers can be studied to understand valuable purchasing patterns.

## Limitations
- The data represents historical transactions from 2010–2011 and does not describe current customer behavior.
- A repeat customer is defined as a customer with more than one recorded invoice in the analysis.
- Recency groups describe the gap since the latest recorded purchase; they do not prove that a customer has permanently stopped buying.
- Customer IDs are anonymized identifiers.

## Project Structure
- `01_inspect_data.py` — Initial data inspection
- `02_investigate_data.py` — Data quality investigation
- `03_clean_data.py` — Data cleaning
- `04_customer_analysis.py` — Customer purchase analysis
- `05_customer_recency.py` — Customer recency analysis
- `06_customer_summary.py` — Customer summary generation
- `cleaned_online_retail.csv` — Cleaned transaction data
- `customer_purchase_counts.csv` — Customer purchase counts
- `customer_recency_analysis.csv` — Customer recency groups
- `customer_summary.csv` — Customer-level summary
- `customer_summary.xlsx` — Excel analysis and visualizations

## Conclusion
This project demonstrates how Python and Excel can be used together to clean retail data, analyze customer purchasing behavior, and derive actionable customer-retention insights.
