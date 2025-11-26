import sqlite3
from tabulate import tabulate

conn = sqlite3.connect("../data/finops.db")
cursor = conn.cursor()

cursor.execute("SELECT service, SUM(value) FROM usage_data GROUP BY service")
weekly = cursor.fetchall()

print(tabulate(weekly, headers=["Service", "Total Usage"]))
