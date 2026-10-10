
import pandas as pd

data = pd.read_excel("Online Retail.xlsx")

# 1. Inspect duplicate records
print("Duplicate rows:", data.duplicated().sum())

# 2. Inspect missing customer IDs
print("\nRows with missing CustomerID:")
print(data[data["CustomerID"].isna()].head())

# 3. Inspect negative quantity records
print("\nNegative quantity examples:")
print(data[data["Quantity"] < 0][
    ["InvoiceNo", "Quantity", "UnitPrice", "CustomerID"]
].head(10))

# 4. Check cancellation invoices
print("\nInvoices starting with C:")
print(data[data["InvoiceNo"].astype(str).str.startswith("C")][
    ["InvoiceNo", "Quantity", "UnitPrice"]
].head(10))

# 5. Inspect missing descriptions
print("\nRows with missing Description:")
print(data[data["Description"].isna()].head())

# 6. Check invalid prices
print("\nZero or negative prices:", (data["UnitPrice"] <= 0).sum())

print("\nInvestigation completed.")
