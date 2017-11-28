# encoding=utf-8

from TradeStrategyBase import TradeStrategyBase


class TradeStrategy1(TradeStrategyBase):
    """
    交易策略1：
    追涨策略，当股价上涨至阀值__buy_change_threshold时买入，
    并持有keep_stock_threshold天
    """
    def __init__(self):
        self.__keep_stock_threshold = 20
        self.__buy_change_threshold = 0.07
        self.keep_stock_day = 0

    def buy_strategy(self, index, trade_day, trade_days):
        if self.keep_stock_day == 0 and trade_day.change > self.__buy_change_threshold:
            self.keep_stock_day += 1
        elif self.keep_stock_day > 0:
            self.keep_stock_day += 1

    def sell_strategy(self, index, trade_day, trade_days):
        if self.keep_stock_day > self.__keep_stock_threshold:
            self.keep_stock_day = 0

    @property
    def buy_change_threshold(self):
        return self.__buy_change_threshold

    @buy_change_threshold.setter
    def buy_change_threshold(self, buy_change_threshold):
        if not isinstance(buy_change_threshold, float):
            raise TypeError('buy_change_threshold must be float!')
        self.__buy_change_threshold = round(buy_change_threshold, 3)

    @property
    def keep_stock_threshold(self):
        return self.__keep_stock_threshold

    @keep_stock_threshold.setter
    def keep_stock_threshold(self, keep_stock_threshold):
        if not isinstance(keep_stock_threshold, int):
            raise TypeError('keep_stock_threshold must be int!')
        elif keep_stock_threshold < 1:
            raise ValueError('keep_stock_threshold must > 0')
        self.__keep_stock_threshold = keep_stock_threshold