from pathlib import Path
import pandas as pd
import yfinance as yf

PERIOD_VALUES = ("1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max")
interval_values = ('1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo')

def get_values():
    return {"Air Liquide": "AI.PA",
            "Dassault Aviation": "AM.PA",
            "L'Oréal": "OR.PA",
            "LVMH": "MC.PA",
            "TotalEnergies": "TTE.PA"}

def extract_data(ticker: str, period: str) -> pd.DataFrame:
    if period not in PERIOD_VALUES:
        raise ValueError(f"{period} not valid")

    interval = '1d'
    if period == '5d':
        interval = '1h'
    elif period == '1d':
        interval = '30m'

    data = yf.download(tickers=ticker, period=period,
                       interval=interval,
                       multi_level_index=False
                       )
    data = data[data["High"] != data["Low"]]

    return data

def symbol_lookup(name:str, exchange:str = "PAR"):
    symbol = None
    result = yf.Search(name)
    for quote in result.quotes:
        if quote['exchange'] == exchange:
            symbol = quote['symbol']

    if symbol is not None:
        return symbol
    else:
        raise LookupError(f"No symbol found for {name}")

def extract_names(path:Path):
    data = pd.read_csv(path, encoding="iso-8859-1", sep=";")
    quotes = {}
    for name in data['libellé']:
        if name not in quotes.keys():
            try:
                symbol = symbol_lookup(name)
                quotes[name] = symbol
            except LookupError:
                print(f"{name} not found")

    print(quotes)

