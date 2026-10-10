
import pandas as pd

# Load the original Excel dataset
data = pd.read_excel("Online Retail.xlsx")

# 1. Dataset size
print("Dataset shape:", data.shape)

# 2. Column names
print("\nColumn names:")
print(data.columns.tolist())

# 3. First five records
print("\nFirst five records:")
print(data.head())

# 4. Missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# 5. Duplicate records
print("\nDuplicate rows:", data.duplicated().sum())

# 6. Quantity analysis
print("\nNegative quantity records:", (data["Quantity"] < 0).sum())
print("Zero quantity records:", (data["Quantity"] == 0).sum())

# 7. Invoice date range
data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])

print("\nEarliest invoice:", data["InvoiceDate"].min())
print("Latest invoice:", data["InvoiceDate"].max())

# 8. Customer count
print("\nUnique customers:", data["CustomerID"].nunique())

print("\nInitial inspection completed.")
