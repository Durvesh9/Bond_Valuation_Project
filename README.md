# **Bond Valuation & Time Series Risk Assessment Dashboard**

A comprehensive **Financial Risk Engine** designed using Python and MySQL.
This project automates the workflow of a quantitative analyst by ingesting raw market data, performing advanced financial valuation (DCF, Duration, Convexity), analyzing market volatility (ADF stationarity tests), and generating a polished Excel dashboard for management reporting.

---

## 🚀 **Key Features**

### **🔄 Automated ETL Pipeline**

* Extracts bond inventory and market rate history from CSV files.
* Loads cleaned data into a MySQL database using SQLAlchemy.

### **💰 Bond Valuation Engine**

Implements advanced financial models including:

* Fair Price calculation using DCF
* Macaulay Duration
* Modified Duration (Interest Rate Risk)
* Convexity (Curvature of Price-Yield Relationship)

### **📉 Market Risk & Time-Series Analysis**

* Rolling mean & volatility estimation using Pandas
* Augmented Dickey-Fuller (ADF) Test
* Stationarity analysis for forecasting quality

### **📊 Automated Reporting**

* Generates a multi-sheet **Excel report** with:

  * Charts
  * Conditional formatting
  * Executive summaries

---

## 🛠️ **Tech Stack**

| Layer           | Tools                                  |
| --------------- | -------------------------------------- |
| Language        | Python 3.14.0                          |
| Database        | MySQL (SQLAlchemy, PyMySQL)            |
| Data Processing | Pandas, NumPy                          |
| Time-Series     | Statsmodels                            |
| Reporting       | OpenPyXL                               |
| Finance Logic   | Custom DCF, Duration, Convexity models |

---

## 📂 **Project Structure**

```
Bond_Valuation_Project/
│
├── main.py                      # 🚀 Entry point: orchestrates the entire workflow
├── config.py                    # ⚙️ Configuration: database credentials
├── db_setup.py                  # 🛠️ Initialize DB and load CSV data
├── requirements.txt             # 📦 Python dependencies
│
├── data/                        # 📊 Raw datasets
│   ├── bonds.csv                # Bond inventory (coupon, maturity, etc.)
│   └── interest_rates.csv       # Historical interest-rate time series
│
├── models/
│   ├── bond_analytics.py        # Financial models (DCF, Duration, Convexity)
│   └── time_series_analysis.py  # ADF & time-series computations
│
└── reporting/
    └── reporting.py             # Excel report generator
```

---

## ⚙️ **Installation & Setup**

### **1. Prerequisites**

* Python **3.8+**
* MySQL Server installed & running

---

### **2. Clone the Repository**

```bash
git clone https://github.com/yourusername/Bond_Valuation_Project.git
cd Bond_Valuation_Project
```

---

### **3. Install Python Dependencies**

```bash
pip install -r requirements.txt
```

---

### **4. Configure Database**

Update your MySQL credentials in `config.py`:

```python
USER = 'root'             # or your custom MySQL user
PASSWORD = 'your_password' 
HOST = 'localhost'
```

---

## 🏃‍♂️ **How to Run the Project**

### **Step 1 — Initialize the Database (Run Once)**

Creates the database (`bond_db`) and loads CSV data:

```bash
python db_setup.py
```

---

### **Step 2 — Execute the Analysis Engine**

Runs the financial models and generates the Excel dashboard:

```bash
python main.py
```

---

## 📊 **Understanding the Output**

The project generates:

### 📁 **Bond_Analysis_Report.xlsx**

### **Sheet 1 — Bond Valuation**

* **Fair Value:** DCF-based fair price
* **Modified Duration:** % price change for +1% interest rate
* **Convexity:** Protection from curvature in price-yield curve

### **Sheet 2 — Time-Series Analysis**

* Daily interest-rate trend
* 20-day rolling mean
* Visual charts
* Stationarity results

### **Sheet 3 — Summary**

* ADF test results
* Interpretation: *Stationary vs Non-Stationary*

---

