from __future__ import annotations
import pandas as pd
import numpy as np

def optimize_power_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """Downcast numéricos para reduzir memória."""
    num_cols = df.select_dtypes(include=['float64','int64']).columns
    for c in num_cols:
        if pd.api.types.is_float_dtype(df[c]):
            df[c] = pd.to_numeric(df[c], downcast='float')
        else:
            df[c] = pd.to_numeric(df[c], downcast='integer')
    return df

def add_datetime(df: pd.DataFrame, date_col='Date', time_col='Time') -> pd.DataFrame:
    dt = pd.to_datetime(df[date_col] + ' ' + df[time_col], format='%d/%m/%Y %H:%M:%S', errors='coerce')
    df = df.assign(datetime=dt).set_index('datetime').sort_index()
    return df

def week_day_name(s: pd.Series) -> pd.Series:
    return s.dt.day_name(locale='en_US')

def add_weekday_column(df: pd.DataFrame, date_col='Date') -> pd.DataFrame:
    d = pd.to_datetime(df[date_col], format='%d/%m/%Y', errors='coerce')
    return df.assign(weekday=d.dt.day_name())

def minmax_scale(df: pd.DataFrame, cols):
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[cols] = scaler.fit_transform(df_scaled[cols])
    return df_scaled, scaler
