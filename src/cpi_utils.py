import pandas_datareader as pdr
from datetime import datetime
import pandas as pd

def fetch_cpi(start_date: str):
    """
    Fetch US CPI data using FRED API.
    start_date: str, %Y-%m-%d
    """
    cpi_data = pdr.get_data_fred("CPIAUCSL", start=datetime.strptime(start_date, "%Y-%m-%d"))
    cpi_data["Inflation"] = cpi_data["CPIAUCSL"].pct_change(12) * 100
    return cpi_data
    
def calculate_quarterly_inflation(cpi_data: pd.DataFrame):
    """
    Calculate the last 4 quarters of YoY inflation.
    cpi_data: pd.DataFrame
    """
    cpi_data = cpi_data.resample("Q").mean()
    recent_quarters = cpi_data.iloc[-4:]
    return recent_quarters[["Inflation"]]
