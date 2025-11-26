import sqlite3
import datetime

conn = sqlite3.connect("../data/finops.db")
cursor = conn.cursor()

today = datetime.date.today().isoformat()

cursor.execute("SELECT service, metric, value FROM usage_data WHERE date = ?", (today,))
usage = cursor.fetchall()

for service, metric, value in usage:
    cursor.execute("SELECT price_per_unit FROM pricing_data WHERE service = ?", (service,))
    price_per_unit = cursor.fetchone()[0]

    estimated_cost = value * price_per_unit

    cursor.execute("INSERT INTO cost_estimated (service, estimated_cost, date) VALUES (?, ?, ?)",
                   (service, estimated_cost, today))

conn.commit()
conn.close()

print("Cost estimation complete!")
