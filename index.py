import os

import pandas as pd
import pandas_ta as ta
from binance.client import Client
from dotenv import load_dotenv

from model.kline import Kline

load_dotenv()
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("API_KEY")


def main():
    client = Client(API_KEY, SECRET_KEY)
    res = client.get_historical_klines(
        "FTTBUSD", Client.KLINE_INTERVAL_1HOUR, limit=1000)
    # # print(res.close_price)

    # Create a DataFrame so 'ta' can be used.
    df = pd.DataFrame(res, columns=["open_time", "open_price", "high_price", "low_price", "close_price", "volume", "close_time",
                      "quote_asset_volume", "number_of_trades", "taker_buy_base_asset_volume", "taker_buy_base_quote_volume", "ignore"])

    ema34 = ta.ema(pd.to_numeric(
        df["close_price"], downcast="float"), length=34)
    print(ema34)
    # help(ta.ema)


if __name__ == "__main__":
    main()
