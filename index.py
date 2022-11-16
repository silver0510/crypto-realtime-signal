from binance.client import Client
import indicators as indis
from trending import Trending
import alert_strategy as Alert
from util import print_json
from constants import *


def main():
    show_trend()


def show_trend():
    symbol = 'ETHUSDT'
    interval = Client.KLINE_INTERVAL_1HOUR
    print(f'Current price: {indis.current_price(symbol)}')
    ema_trend = Alert.ma_trending_prime_ma_for_15_1_4(symbol)
    print_json(ema_trend["trend_consensus"])
    print(
        f'Prime ema: {ema_trend["prime_ema"]["ema"]}, Current value = {ema_trend["prime_ema"]["current_value"]}, Trust percent = {ema_trend["prime_ema"]["percent"]}, Price often {ema_trend["prime_ema"]["trend"]}')
    print(f'RSI: {ema_trend["rsi"]}, ATR: {ema_trend["atr"]}')


def get_top_10():
    lis_coin_with_USDT = list(map(lambda x: x["symbol"], list(filter(lambda x: x["quoteAsset"] ==
                                                                     "USDT", client.get_exchange_info()["symbols"]))))
    # print_json(info)
    # avg_price = client.get_avg_price(symbol='BNBUSDT')
    # print(avg_price)
    info_24h = []
    for coin in lis_coin_with_USDT:
        info_24h.append(client.get_ticker(symbol=coin))

    top_10 = sorted(info_24h, key=lambda x: float(
        x["quoteVolume"]), reverse=True)[:20]
    print_json(top_10)


if __name__ == "__main__":
    main()
