# US CPI Inflation Data Fetcher

This project fetches the latest US CPI data and calculates the last 4 quarters of inflation. It uses the `pandas_datareader` package to retrieve CPI data from FRED and outputs the inflation for the most recent 4 quarters.

## Repository URL

You can access the repository here: [GitHub Repository](https://github.com/FinanStudent/phbs-qps-2024)

## Requirements

Before running the code, ensure you have the following:

- Python 3.8
- pip (Python package manager)

### To Run the Code

1. **Clone the Repository**  

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

2. **Set Up a Virtual Environment**

It's recommended to create a virtual environment to isolate the project dependencies:

```bash
python -m venv venv
```

3. **Activate the Virtual Environment**

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

4. **Install Dependencies**

Install the necessary dependencies listed in requirements.txt:

```bash
pip install -r requirements.txt
```

5. **Run the Code**

The script to fetch CPI data and calculate inflation can be found in the scripts folder. To execute the code:

```bash
python scripts/fetch_cpi.py
```

6. **View Results**

The output will display the inflation for the last 4 quarters.

**Notes**
This project uses the FRED API to fetch CPI data, so an internet connection is required to run the code.
If you encounter any issues, make sure all dependencies are installed and that you have a working internet connection.

**License**

This project is licensed under the MIT License - see the LICENSE file for details.
