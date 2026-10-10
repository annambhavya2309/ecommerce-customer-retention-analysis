
import pandas as pd

data = pd.read_csv("cleaned_online_retail.csv")
data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])

analysis_date = data["InvoiceDate"].max().normalize()

summary = data.groupby("CustomerID").agg(
    TotalInvoices=("InvoiceNo", "nunique"),
    TotalQuantity=("Quantity", "sum"),
    TotalSpend=("SalesAmount", "sum"),
    LastPurchaseDate=("InvoiceDate", "max")
).reset_index()

summary["DaysSinceLastPurchase"] = (
    analysis_date - summary["LastPurchaseDate"].dt.normalize()
).dt.days

summary["CustomerType"] = summary["TotalInvoices"].apply(
    lambda count: "Repeat Customer" if count > 1 else "One-Time Customer"
)

summary.to_csv("customer_summary.csv", index=False)

print("Customer summary created.")
print("Total customers:", len(summary))
print("\nCustomer type counts:")
print(summary["CustomerType"].value_counts())

print("\nTop 10 customers by total spend:")
print(
    summary.sort_values("TotalSpend", ascending=False)
    .head(10)[["CustomerID", "TotalInvoices", "TotalSpend"]]
    .to_string(index=False)
)
