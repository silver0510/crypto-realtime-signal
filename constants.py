import os

from binance.client import Client
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("API_KEY")
client = Client(API_KEY, SECRET_KEY)

KLINE_FORMAT = ["open_time", "open_price", "high_price", "low_price", "close_price", "volume", "close_time",
                "quote_asset_volume", "number_of_trades", "taker_buy_base_asset_volume", "taker_buy_base_quote_volume", "ignore"]
