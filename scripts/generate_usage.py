import sqlite3
import datetime
import random

conn = sqlite3.connect("../data/finops.db")
cursor = conn.cursor()

today = datetime.date.today().isoformat()

usage_samples = {
    "S3": ("GB_Stored", random.uniform(1, 8)),        # 1–8 GB
    "EC2": ("Hours_Run", random.uniform(100, 900)),   # 100–900 hrs
    "Lambda": ("Invocations", random.randint(100000, 1500000))
}

for service, (metric, value) in usage_samples.items():
    cursor.execute("INSERT INTO usage_data (service, metric, value, date) VALUES (?, ?, ?, ?)",
                   (service, metric, value, today))

conn.commit()
conn.close()

print("Daily mock usage added!")
