from binance.client import Client
import indicators as indis
from trending import Trending


def main():
    symbol = 'GMXUSDT'
    # ret = indis.calc_current_ema('FTTBUSD', Client.KLINE_INTERVAL_15MINUTE, 89)
    trend = Trending.detect_trend_interval(
        symbol, Client.KLINE_INTERVAL_1HOUR)
    print(trend)
    trend_consensus = Trending.current_trend_15_1_4(symbol)
    print(trend_consensus)
    ema, percent = Trending.prime_ema_interval(
        symbol, Client.KLINE_INTERVAL_1HOUR)
    print(ema, percent)


if __name__ == "__main__":
    main()
