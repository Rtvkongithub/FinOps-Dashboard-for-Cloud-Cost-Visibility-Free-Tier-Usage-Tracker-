import requests
import sqlite3

conn = sqlite3.connect("../data/finops.db")
cursor = conn.cursor()

pricing_api = "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/index.json"

print("Fetching AWS pricing...")
data = requests.get(pricing_api).json()

# Example services
service_prices = {
    "S3": 0.023,           # per GB (standard)
    "EC2": 0.0116,         # t2.micro per hour us-east-1
    "Lambda": 0.0000002    # per invocation
}

for service, price in service_prices.items():
    cursor.execute("INSERT INTO pricing_data (service, unit, price_per_unit) VALUES (?, ?, ?)",
                   (service, "unit", price))

conn.commit()
conn.close()
print("Pricing updated!")
