import os
import sys
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))  # Add src to path
from cpi_utils import *

if __name__ == "__main__":
    cpi_data = fetch_cpi(start_date="2023-01-01")
    quarterly_inflation = calculate_quarterly_inflation(cpi_data)
    print("Last 4 Quarters of US Inflation:")
    print(quarterly_inflation)
