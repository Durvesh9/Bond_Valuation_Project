import numpy as np
import pandas as pd

# This file contains the pure financial mathematics

def calculate_bond_price(coupon_rate, maturity_years, ytm, par_value, freq):
    try:
        periods = maturity_years * freq
        coupon_payment = (coupon_rate * par_value) / freq
        discount_rate = ytm / freq
        
        coupon_pv = coupon_payment * (1 - (1 + discount_rate)**-periods) / discount_rate
        par_pv = par_value / (1 + discount_rate)**periods
        return round(coupon_pv + par_pv, 2)
    except:
        return np.nan

def calculate_macaulay_duration(coupon_rate, maturity_years, ytm, par_value, freq, price):
    try:
        periods = maturity_years * freq
        coupon_payment = (coupon_rate * par_value) / freq
        discount_rate = ytm / freq
        weighted_time_sum = 0
        
        for t in range(1, int(periods) + 1):
            cash_flow = coupon_payment + par_value if t == periods else coupon_payment
            pv_cash_flow = cash_flow / (1 + discount_rate)**t
            weighted_time_sum += (t * pv_cash_flow)
            
        return round((weighted_time_sum / price) / freq, 4)
    except:
        return np.nan

def calculate_modified_duration(macaulay_duration, ytm, freq):
    try:
        return round(macaulay_duration / (1 + (ytm / freq)), 4)
    except:
        return np.nan

def calculate_convexity(coupon_rate, maturity_years, ytm, par_value, freq, price):
    try:
        periods = maturity_years * freq
        coupon_payment = (coupon_rate * par_value) / freq
        discount_rate = ytm / freq
        convexity_sum = 0
        
        for t in range(1, int(periods) + 1):
            cash_flow = coupon_payment + par_value if t == periods else coupon_payment
            pv_cash_flow = cash_flow / (1 + discount_rate)**t
            convexity_sum += (pv_cash_flow * t * (t + 1))
            
        convexity = (convexity_sum / (price * (1 + discount_rate)**2))
        return round(convexity / (freq**2), 4)
    except:
        return np.nan

def analyze_bonds(bonds_df, market_ytm):
    print(f"Calculating metrics for {len(bonds_df)} bonds...")
    results = bonds_df.copy()
    
    results['price'] = results.apply(lambda row: calculate_bond_price(
        row['coupon_rate'], row['maturity_years'], market_ytm, row['par_value'], row['payment_frequency']), axis=1)
        
    results['macaulay_duration'] = results.apply(lambda row: calculate_macaulay_duration(
        row['coupon_rate'], row['maturity_years'], market_ytm, row['par_value'], row['payment_frequency'], row['price']), axis=1)
        
    results['modified_duration'] = results.apply(lambda row: calculate_modified_duration(
        row['macaulay_duration'], market_ytm, row['payment_frequency']), axis=1)
        
    results['convexity'] = results.apply(lambda row: calculate_convexity(
        row['coupon_rate'], row['maturity_years'], market_ytm, row['par_value'], row['payment_frequency'], row['price']), axis=1)
        
    return results