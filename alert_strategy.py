from binance.client import Client

import indicators
from trending import Trending


def ma_trending_prime_ma_for_15_1_4(symbol):
    return __ma_trending_prime_ma(symbol, Trending.current_trend_15_1_4, Client.KLINE_INTERVAL_15MINUTE)


def ma_trending_prime_ma_for_1_4_1(symbol):
    return __ma_trending_prime_ma(symbol, Trending.current_trend_1_4_1, Client.KLINE_INTERVAL_1HOUR)


def __ma_trending_prime_ma(symbol, trend_consensus_func, short_trend_interval):
    trend_consensus = trend_consensus_func(symbol)
    ema, percent = Trending.prime_ema_interval(
        symbol, short_trend_interval)
    return {
        "trend_consensus": trend_consensus,
        "prime_ema": {
            "ema": ema,
            "percent": percent
        }
    }
