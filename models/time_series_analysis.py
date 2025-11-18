import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt

# This file contains the statistical tests logic

def analyze_interest_rates(rates_df, rolling_window=20, acf_lags=40):
    print("Analyzing interest rate time series...")
    ts_df = rates_df.copy().set_index('date').sort_index()
    
    # 1. Statistics
    ts_df[f'rolling_mean_{rolling_window}d'] = ts_df['rate'].rolling(window=rolling_window).mean()
    ts_df['pct_change'] = ts_df['rate'].pct_change()
    ts_df = ts_df.fillna(0)
    
    # 2. ADF Test (Stationarity)
    adf_series = ts_df['rate'].diff().dropna()
    adf_result = adfuller(adf_series)
    
    adf_output = {
        'test_on': 'First Difference of Rate',
        'adf_statistic': adf_result[0],
        'p_value': adf_result[1],
        'lags_used': adf_result[2],
        'is_stationary_at_5%': 'Yes' if adf_result[1] < 0.05 else 'No'
    }
    print(f"ADF P-Value: {adf_output['p_value']:.5f} (Stationary: {adf_output['is_stationary_at_5%']})")
    
    # 3. ACF Plot
    plot_filename = 'acf_plot.png'
    try:
        fig, ax = plt.subplots(figsize=(10, 5))
        plot_acf(adf_series, lags=acf_lags, ax=ax, title='Autocorrelation (ACF)')
        plt.savefig(plot_filename)
        plt.close(fig)
    except Exception as e:
        print(f"Error plotting ACF: {e}")
        plot_filename = None

    return ts_df.reset_index(), adf_output, plot_filename