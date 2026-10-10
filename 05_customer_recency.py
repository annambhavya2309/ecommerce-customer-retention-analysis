
import pandas as pd

data = pd.read_csv("cleaned_online_retail.csv")
data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])

# Last recorded date in the dataset
analysis_date = data["InvoiceDate"].max().normalize()

# Find each customer's most recent purchase
last_purchase = data.groupby("CustomerID")["InvoiceDate"].max()

# Calculate days since last purchase
days_since_purchase = (analysis_date - last_purchase.dt.normalize()).dt.days

customer_recency = pd.DataFrame({
    "LastPurchaseDate": last_purchase,
    "DaysSinceLastPurchase": days_since_purchase
})

# Group customers by recency
customer_recency["RecencyGroup"] = pd.cut(
    customer_recency["DaysSinceLastPurchase"],
    bins=[-1, 30, 90, 180, float("inf")],
    labels=["0-30 days", "31-90 days", "91-180 days", "180+ days"]
)

print("Analysis date:", analysis_date)
print("\nCustomers by recency group:")
print(customer_recency["RecencyGroup"].value_counts().sort_index())

customer_recency.to_csv("customer_recency_analysis.csv")

print("\nRecency analysis completed.")
