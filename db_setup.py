import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text, exc
from config import DB_URL, DB_URL_WITH_DB, DATABASE

def setup_database():
    """Creates the database, tables, and populates them with data from CSV files."""
    try:
        # 1. Connect to Server and Create Database
        engine = create_engine(DB_URL)
        with engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DATABASE}"))
            conn.commit()
            print(f"Database '{DATABASE}' checked/created.")

        # 2. Connect to specific Database
        db_engine = create_engine(DB_URL_WITH_DB)
        
        # 3. Load Bonds CSV
        try:
            bonds_df = pd.read_csv(r'data\bonds.csv')
            bonds_df.to_sql('bonds', db_engine, if_exists='replace', index=False)
            print(f"Uploaded {len(bonds_df)} bonds to SQL.")
        except FileNotFoundError:
            print("Error: `bonds.csv` not found.")
            return

        # 4. Load Interest Rates CSV
        try:
            rates_df = pd.read_csv('data/interest_rates.csv')
            rates_df.to_sql('interest_rates', db_engine, if_exists='replace', index=False)
            print(f"Uploaded {len(rates_df)} rates to SQL.")
        except FileNotFoundError:
            print("Error: `interest_rates.csv` not found.")
            return
        
        print("Database setup complete!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    setup_database()