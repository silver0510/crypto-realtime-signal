from binance.client import Client
import util

import constants as cons
import indicators as indis
from model.kline import Kline


class Trending():
    SHORT_LENGTH = 34
    MEDIUM_LENGTH = 89
    LONG_LENGTH = 200
    UP_TREND = 'UP TREND'
    SIDE_WAY = 'SIDE WAY'
    DOWN_TREND = 'DOWN TREND'

    @classmethod
    def detect_trend_interval(self, symbol='BTCBUSD', kline_interval=Client.KLINE_INTERVAL_1DAY):
        current_price = self.__current_price(symbol)
        ema_short = indis.calc_current_ema(
            symbol, kline_interval, self.SHORT_LENGTH)
        ema_medium = indis.calc_current_ema(
            symbol, kline_interval, self.MEDIUM_LENGTH)
        # ema_long = indis.calc_current_ema(
        #     symbol, kline_interval, self.LONG_LENGTH)

        if (current_price >= ema_short) and (current_price >= ema_medium):
            return self.UP_TREND
        if (current_price <= ema_short) and (current_price <= ema_medium):
            return self.DOWN_TREND

        return self.SIDE_WAY

    '''
        Trending for 15min - 1h - 4h
    '''
    @ classmethod
    def current_trend_15_1_4(self, symbol='BTCBUSD'):
        return self.__trend_short_medium_long_consensus(self, symbol, Client.KLINE_INTERVAL_15MINUTE, Client.KLINE_INTERVAL_1HOUR, Client.KLINE_INTERVAL_4HOUR)

    '''
        Trending for 1h - 4h - 1day
    '''
    @ classmethod
    def current_trend_1_4_1(self, symbol='BTCBUSD',):
        return self.__trend_short_medium_long_consensus(self, symbol, Client.KLINE_INTERVAL_1HOUR, Client.KLINE_INTERVAL_4HOUR, Client.KLINE_INTERVAL_1DAY)

    def __trend_short_medium_long_consensus(self, symbol, short_interval, medium_interval, long_interval):
        short_trend = self.detect_trend_interval(
            symbol, short_interval)

        medium_trend = self.detect_trend_interval(
            symbol, medium_interval)
        long_trend = self.detect_trend_interval(
            symbol, long_interval)

        conclusion = self.SIDE_WAY
        if (short_trend == self.UP_TREND) and (medium_trend == self.UP_TREND) and (long_trend == self.UP_TREND):
            conclusion = self.UP_TREND

        if (short_trend == self.DOWN_TREND) and (medium_trend == self.DOWN_TREND) and (long_trend == self.DOWN_TREND):
            conclusion = self.DOWN_TREND

        return {
            "short_trend": short_trend,
            "medium_trend": medium_trend,
            "long_trend": long_trend,
            "conclusion": conclusion
        }

    @ classmethod
    def prime_ema_interval(self, symbol='BTCBUSD', kline_interval=Client.KLINE_INTERVAL_1DAY):
        ema_lengths = [20, 34, 55, 84, 200]
        for ema_length in ema_lengths:
            ema, is_important, percent = self.__is_ema_important(
                symbol, kline_interval, ema_length)
            if is_important:
                return ema, percent
        return None, None

    def __is_ema_important(symbol='BTCBUSD', kline_interval=Client.KLINE_INTERVAL_1DAY, length=34):
        CHECKING_LENGTH = 60
        THRESHOLD = 0.8
        prices, emas = indis.calc_1000_ema(symbol, kline_interval, length)
        above_ema = []
        below_ema = []
        for i in range(1, CHECKING_LENGTH + 1):
            if prices[len(prices)-i] >= emas[len(prices)-i]:
                above_ema.append((prices[len(prices)-i], emas[len(prices)-i]))
            else:
                below_ema.append((prices[len(prices)-i], emas[len(prices)-i]))
        percents_of_above_ema = round(len(above_ema)/CHECKING_LENGTH, 2)
        percents_of_below_ema = round(len(below_ema)/CHECKING_LENGTH, 2)
        if (percents_of_above_ema > THRESHOLD) or (percents_of_below_ema > THRESHOLD):
            return length, True, max(percents_of_above_ema, percents_of_below_ema)
        else:
            return length, False, max(percents_of_above_ema, percents_of_below_ema)

    def __current_price(symbol):
        return Kline(cons.client.get_historical_klines(
            symbol, interval=Client.KLINE_INTERVAL_30MINUTE, limit=1)[0]).close_price
