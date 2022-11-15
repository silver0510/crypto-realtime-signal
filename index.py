from binance.client import Client
import indicators as indis
from trending import Trending
import alert_strategy as Alert
from util import print_json


def main():
    symbol = 'BTCUSDT'
    interval = Client.KLINE_INTERVAL_1HOUR
    ema_trend = Alert.ma_trending_prime_ma_for_1_4_1(symbol)
    print_json(ema_trend["trend_consensus"])
    print(
        f'prime ema: {ema_trend["prime_ema"]["ema"]}, current value = {ema_trend["prime_ema"]["current_value"]}, trust percent = {ema_trend["prime_ema"]["percent"]}')
    print(f'RSI: {ema_trend["rsi"]}, ATR: {ema_trend["atr"]}')


if __name__ == "__main__":
    main()
