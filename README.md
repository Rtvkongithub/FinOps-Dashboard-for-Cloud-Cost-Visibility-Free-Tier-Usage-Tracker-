# FinOps Dashboard: Cloud Cost Visibility (Free-Tier Usage Tracker)

🌟 Project Overview

This project simulates a **FinOps (Financial Operations) Dashboard** to monitor cloud resource usage and estimated costs, with alerts for approaching free-tier limits.  
It is fully functional **without an active AWS Free Tier account** by using mock usage data and AWS pricing API.

 🗂️ Folder Structure

finops-dashboard/
│
├── data/
│ └── finops.db # SQLite database storing usage, pricing, costs, and alerts
│
├── scripts/
│ ├── fetch_pricing.py # Fetches AWS pricing from public API
│ ├── generate_usage.py # Generates daily mock usage data
│ ├── calculate_costs.py # Calculates estimated costs
│ ├── check_alerts.py # Checks free-tier thresholds and logs alerts
│ └── weekly_report.py # Generates weekly usage report
│
└── docs/
└── alert_rules.md # Free-tier limits and alert rules documentation
 🛠️ Tools Used

- **Python** (for scripts)  
- **SQLite** (for storing data locally)  
- **Grafana** (for visualization)  
- **AWS Pricing API** (free, public API for pricing data)  



 Features

- Simulates cloud service usage (S3, EC2, Lambda)  
- Calculates estimated costs using pricing data  
- Stores data in SQLite (`finops.db`)  
- Generates alerts when approaching free-tier limits  
- Weekly usage report via Python script  
- Visualized in Grafana (charts for usage, costs, alerts)  

---

 📝 Free-Tier Alert Rules

Example thresholds used (mocked for demo purposes):

| Service | Free Tier Limit | Alert Threshold |
|---------|----------------|----------------|
| S3      | 5 GB           | 4 GB           |
| EC2     | 750 hrs        | 600 hrs        |
| Lambda  | 1,000,000 calls| 800,000 calls  |

All thresholds are configurable in `check_alerts.py` and `alert_rules.md`.

---

## 🚀 Setup Instructions

### 1. Clone Repository
git clone <your-repo-url>
cd finops-dashboard
2. Install Python Dependencies
bash
Copy code
pip install sqlite3 datetime requests tabulate matplotlib
3. Create SQLite DB
bash
Copy code
sqlite3 data/finops.db
Paste this schema:

sql
Copy code
CREATE TABLE usage_data (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  service TEXT,
  metric TEXT,
  value REAL,
  date TEXT
);

CREATE TABLE pricing_data (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  service TEXT,
  unit TEXT,
  price_per_unit REAL
);

CREATE TABLE cost_estimated (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  service TEXT,
  estimated_cost REAL,
  date TEXT
);

CREATE TABLE alerts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  service TEXT,
  message TEXT,
  date TEXT
);
Exit with .exit

4. Run Python Scripts
bash
Copy code
python3 scripts/fetch_pricing.py     # Fetch AWS pricing
python3 scripts/generate_usage.py    # Generate mock usage
python3 scripts/calculate_costs.py   # Calculate estimated costs
python3 scripts/check_alerts.py      # Generate alerts
python3 scripts/weekly_report.py     # Show weekly report
5. Configure Grafana
Install Grafana (https://grafana.com/grafana/download)

Install SQLite plugin:

bash
Copy code
sudo grafana-cli plugins install frser-sqlite-datasource
sudo systemctl restart grafana-server
Open Grafana → Data Sources → Add SQLite

Set Database Path to absolute path:

swift
Copy code
/var/lib/grafana/finops-dashboard/finops.db
Click Save & Test → should show “Data source is working”

Create dashboards / panels for usage_data, cost_estimated, alerts

📊 Sample Panels
Daily Usage → Bar chart for S3/EC2/Lambda usage

Estimated Cost → Line chart per service

Alerts Table → Shows services approaching free-tier limits

💡 Notes
All usage data is mocked; can be replaced with real AWS usage data when available

Free-tier thresholds are configurable in check_alerts.py

Ensure Grafana has read permission for the SQLite DB

🏆 Deliverables
Python scripts for fetching pricing, generating usage, calculating costs, and alerts

SQLite database (finops.db)

Grafana dashboards with usage, cost, and alerts

Weekly usage report

Free-tier alert documentation (alert_rules.md)

