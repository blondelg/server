import sys  
print(sys.path)
from mail_client.mail_client import Client
from kraken.api import get_btc_price
from datetime import date


def exec():
    today = date.today()
    str_date = today.strftime("%Y-%m-%d") 
    price = get_btc_price()
    open = str(round(float(price["o"]), 2))
    high = str(round(float(price["h"][1]), 2))
    low = str(round(float(price["l"][1]), 2))
    message = f"open: {open} \nhigh: {high} \nlow: {low} "
    message = message + "\n https://www.kraken.com/prices/xbt-bitcoin-price-chart/eur-euro?interval=1y" 
    Client().send("geoffroy.blondel@gmail.com", f"[BTC-EUR] {str_date} last 24h", message)

if __name__ == "__main__":
    exec()