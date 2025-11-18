import pandas as pd
from sqlalchemy import create_engine
from config import DB_URL_WITH_DB
from models import bond_analytics, time_series_analysis
from reporting import reporting

# Config
OUTPUT_REPORT = 'Bond_Analysis_Report.xlsx'
MARKET_YTM = 0.05

def load_data(engine):
    try:
        print("Loading data from database...")
        bonds_df = pd.read_sql("SELECT * FROM bonds", engine)
        rates_df = pd.read_sql("SELECT * FROM interest_rates ORDER BY date", engine)
        rates_df['date'] = pd.to_datetime(rates_df['date'])
        return bonds_df, rates_df
    except Exception as e:
        print(f"Data loading failed: {e}")
        return None, None

def main():
    print("--- Starting Analysis ---")
    
    # 1. Connect
    try:
        engine = create_engine(DB_URL_WITH_DB)
        with engine.connect() as conn: pass # Test connection
    except Exception as e:
        print(f"Database connection failed: {e}")
        return

    # 2. Load
    bonds_df, rates_df = load_data(engine)
    if bonds_df is None: return

    # 3. Analyze Bonds
    bond_results = bond_analytics.analyze_bonds(bonds_df, MARKET_YTM)

    # 4. Analyze Time Series
    ts_results, adf_results, acf_path = time_series_analysis.analyze_interest_rates(rates_df)

    # 5. Report
    reporting.create_report(bond_results, ts_results, adf_results, acf_path, OUTPUT_REPORT)
    
    print("--- Workflow Complete ---")

if __name__ == "__main__":
    main()