import sqlite3
import datetime

conn = sqlite3.connect("../data/finops.db")
cursor = conn.cursor()

today = datetime.date.today().isoformat()

cursor.execute("SELECT service, value FROM usage_data WHERE date = ?", (today,))
usage = cursor.fetchall()

limits = {
    "S3": 5,
    "EC2": 750,
    "Lambda": 1000000
}

threshold = {
    "S3": 4,
    "EC2": 600,
    "Lambda": 800000
}

for service, value in usage:
    if value > threshold[service]:
        msg = f"{service} usage {value} is close to free-tier limit!"
        cursor.execute("INSERT INTO alerts (service, message, date) VALUES (?, ?, ?)",
                       (service, msg, today))

conn.commit()
conn.close()
print("Alert check complete!")
