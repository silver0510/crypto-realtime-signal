import pandas as pd
import pandas_ta as ta
from binance.client import Client

import constants as cons
from model.kline import Kline


def calc_current_ema(symbol='BTCBUSD', kline_interval=Client.KLINE_INTERVAL_1DAY, length=34):
    df = pd.DataFrame(cons.client.get_historical_klines(
        symbol, kline_interval, limit=1000), columns=cons.KLINE_FORMAT)

    ret = ta.ema(pd.to_numeric(
        df["close_price"], downcast="float"), length=length)
    return ret[len(ret) - 1]
