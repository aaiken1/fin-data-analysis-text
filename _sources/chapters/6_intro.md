# Data APIs

In finance, data is everything. Whether you're analyzing stock prices, economic indicators, housing markets, or alternative data, you need reliable ways to access and import data into your Python environment.

This chapter introduces you to **Application Programming Interfaces (APIs)** - the standard way that applications communicate with remote data sources. APIs let you programmatically request data from servers, often in real-time, without manually downloading files.

## Why Use APIs?

- **Automation**: Schedule data pulls without manual intervention
- **Real-time data**: Access the latest information as it becomes available
- **Reproducibility**: Your code documents exactly what data you retrieved
- **Scale**: Download large datasets programmatically

## API Keys and Security

Most data APIs require an **API key** - a unique identifier that authenticates your requests.

```{warning}
**Never hardcode your API key in your scripts!** If you share your code (e.g., push to GitHub), your key could be exposed.
```

Instead, use one of these secure methods:

1. **Environment variables** - Store keys in your system's environment
2. **GitHub Secrets** - For GitHub Codespaces, store keys as repository secrets
3. **`.env` files** - Local files (never committed to git) that store your keys

Example of secure API key usage:

```python
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file
API_KEY = os.getenv('MY_API_KEY')
```

## Data Sources Covered

This chapter covers several important data APIs for finance:

```{tableofcontents}
```

### FRED

The **Federal Reserve Economic Data (FRED)** API provides access to hundreds of thousands of economic time series - GDP, inflation, interest rates, employment data, and more.

### NASDAQ Data Link

Formerly known as Quandl, **NASDAQ Data Link** offers both free and premium financial datasets, including Zillow housing data, futures data, and various alternative data sources.

### Databento

**Databento** is a modern market data platform providing high-quality historical and real-time data for equities, futures, and options. It's designed for quantitative research and algorithmic trading.

### WRDS

**Wharton Research Data Services (WRDS)** is the gold standard for academic financial research. It provides access to CRSP, Compustat, IBES, and dozens of other research databases. Access typically requires institutional affiliation.

## General API Workflow

Most API interactions follow this pattern:

1. **Authenticate** - Provide your API key
2. **Request** - Specify what data you want (ticker, date range, etc.)
3. **Receive** - Get data back, often in JSON format
4. **Transform** - Convert to a pandas DataFrame for analysis

```python
# General pattern
import requests

response = requests.get(
    url="https://api.example.com/data",
    headers={"Authorization": f"Bearer {API_KEY}"},
    params={"symbol": "AAPL", "start": "2024-01-01"}
)

data = response.json()
df = pd.DataFrame(data)
```

## Rate Limits and Best Practices

Most APIs have **rate limits** - restrictions on how many requests you can make per minute/hour/day. Best practices:

- **Cache your data**: Don't re-download what you already have
- **Be patient**: Add delays between requests if needed
- **Read the docs**: Each API has different limits and requirements
- **Handle errors gracefully**: Network requests can fail

Let's explore each data source in detail.
