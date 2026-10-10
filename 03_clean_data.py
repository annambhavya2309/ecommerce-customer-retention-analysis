
import pandas as pd

data = pd.read_excel("Online Retail.xlsx")

print("Original rows:", len(data))

# 1. Remove exact duplicate rows
data = data.drop_duplicates()
print("After removing duplicates:", len(data))

# 2. Convert columns to appropriate data types
data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])
data["CustomerID"] = data["CustomerID"].astype("Int64")

# 3. Identify cancellation invoices
data["InvoiceNo"] = data["InvoiceNo"].astype(str)
data["IsCancellation"] = data["InvoiceNo"].str.startswith("C")

print("Cancellation invoice rows:", data["IsCancellation"].sum())

# 4. Separate records suitable for customer-level sales analysis
sales = data[
    data["CustomerID"].notna()
    & (~data["IsCancellation"])
    & (data["Quantity"] > 0)
    & (data["UnitPrice"] > 0)
].copy()

# 5. Calculate transaction value
sales["SalesAmount"] = sales["Quantity"] * sales["UnitPrice"]

# 6. Save cleaned data
sales.to_csv("cleaned_online_retail.csv", index=False)

print("Rows for customer sales analysis:", len(sales))
print("Unique customers:", sales["CustomerID"].nunique())
print("Total sales value:", round(sales["SalesAmount"].sum(), 2))
print("Cleaned dataset saved successfully.")
