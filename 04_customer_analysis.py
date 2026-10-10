
import pandas as pd

data = pd.read_csv("cleaned_online_retail.csv")

data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])

# Count distinct purchase invoices for each customer
customer_purchases = data.groupby("CustomerID")["InvoiceNo"].nunique()

# Separate repeat and one-time customers
repeat_customers = customer_purchases[customer_purchases > 1]
one_time_customers = customer_purchases[customer_purchases == 1]

total_customers = len(customer_purchases)
repeat_count = len(repeat_customers)
one_time_count = len(one_time_customers)

repeat_percentage = (repeat_count / total_customers) * 100
one_time_percentage = (one_time_count / total_customers) * 100

print("Total customers:", total_customers)
print("Repeat customers:", repeat_count)
print("One-time customers:", one_time_count)
print("Repeat customer percentage:", round(repeat_percentage, 2), "%")
print("One-time customer percentage:", round(one_time_percentage, 2), "%")

# Save purchase counts for further analysis
customer_purchases.to_csv("customer_purchase_counts.csv", header=["InvoiceCount"])

print("\nCustomer purchase analysis completed.")
