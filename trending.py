from binance.client import Client
import indicators as indis
import pandas as pd
import pandas_ta as ta


class Trending():
    SHORT_LENGTH = 34
    MEDIUM_LENGTH = 89
    LONG_LENGTH = 200
    UP_TREND = 'UP TREND'
    SIDE_WAY = 'SIDE WAY'
    DOWN_TREND = 'DOWN TREND'

    @classmethod
    def detect_trend_interval(self, symbol='BTCBUSD', kline_interval=Client.KLINE_INTERVAL_1DAY):
        ema_short = indis.calc_current_ema(
            symbol, kline_interval, self.SHORT_LENGTH)
        ema_medium = indis.calc_current_ema(
            symbol, kline_interval, self.MEDIUM_LENGTH)
        ema_long = indis.calc_current_ema(
            symbol, kline_interval, self.LONG_LENGTH)

        if ema_short < ema_medium < ema_long:
            return self.DOWN_TREND
        if ema_short > ema_medium > ema_long:
            return self.UP_TREND

        return self.SIDE_WAY

    '''
        Trending for 15min - 1h - 4h
    '''
    @classmethod
    def current_trend_15_1_4(self, symbol='BTCBUSD'):
        return self.__trend_short_medium_long_consensus(self, symbol, Client.KLINE_INTERVAL_15MINUTE, Client.KLINE_INTERVAL_1HOUR, Client.KLINE_INTERVAL_4HOUR)

    '''
        Trending for 1h - 4h - 1day
    '''
    @classmethod
    def current_trend_1_4_1(self, symbol='BTCBUSD',):
        return self.__trend_short_medium_long_consensus(self, symbol, Client.KLINE_INTERVAL_1HOUR, Client.KLINE_INTERVAL_4HOUR, Client.KLINE_INTERVAL_1DAY)

    def __trend_short_medium_long_consensus(self, symbol, short_interval, medium_interval, long_interval):
        short_trend = self.detect_trend_interval(
            symbol, short_interval)

        medium_trend = self.detect_trend_interval(
            symbol, medium_interval)
        long_trend = self.detect_trend_interval(
            symbol, long_interval)

        if (short_trend == self.UP_TREND) and (medium_trend == self.UP_TREND) and (long_trend == self.UP_TREND):
            return self.UP_TREND

        if (short_trend == self.DOWN_TREND) and (medium_trend == self.DOWN_TREND) and (long_trend == self.DOWN_TREND):
            return self.DOWN_TREND

        return self.SIDE_WAY

    @classmethod
    def prime_ema_interval(self, symbol='BTCBUSD', kline_interval=Client.KLINE_INTERVAL_1DAY):
        CHECKING_LENGTH = 60
        prices, emas = indis.calc_1000_ema(symbol, kline_interval)
        above_ema = []
        below_ema = []
        for i in range(1, CHECKING_LENGTH):
            if prices[len(prices)-i] >= emas[len(prices)-i]:
                below_ema.append((prices[len(prices)-i], emas[len(prices)-i]))
            else:
                below_ema.append((prices[len(prices)-i], emas[len(prices)-i]))
        print(len(above_ema))
        print(below_ema)
