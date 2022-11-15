from binance.client import Client
import indicators as indis
from trending import Trending
import alert_strategy as Alert
from util import print_json


def main():
    symbol = 'BTCUSDT'
    interval = Client.KLINE_INTERVAL_1HOUR
    print(f'Current price: {indis.current_price(symbol)}')
    ema_trend = Alert.ma_trending_prime_ma_for_1_4_1(symbol)
    print_json(ema_trend["trend_consensus"])
    print(
        f'Prime ema: {ema_trend["prime_ema"]["ema"]}, Current value = {ema_trend["prime_ema"]["current_value"]}, Trust percent = {ema_trend["prime_ema"]["percent"]}, Price often {ema_trend["prime_ema"]["trend"]}')
    print(f'RSI: {ema_trend["rsi"]}, ATR: {ema_trend["atr"]}')


if __name__ == "__main__":
    main()
