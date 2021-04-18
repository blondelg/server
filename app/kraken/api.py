import requests

KRAKEN_DATA_LABELS = {
  "a": "Ask",
  "b": "Bid",
  "c": "Last Trade Closed",
  "v": "Volume",
  "l": "Low",
  "h": "High",
  "o": "Today Opening Price"
}

def get_btc_price():
    return requests.get("https://api.kraken.com/0/public/Ticker?pair=XXBTZEUR").json()['result']['XXBTZEUR']