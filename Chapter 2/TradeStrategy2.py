#encoding=utf-8

from TradeStrategyBase import TradeStrategyBase


class TradeStrategy2(TradeStrategyBase):

    keep_day_threshold = 10
    buy_change_threshold = -0.10

    def __init__(self):
        self.keep_stock_day = 0

    def buy_strategy(self, index, day, days):
        if self.keep_stock_day == 0 and index >= 1:
            today_down = day.change < 0
            yesterday_down = days[index-1].change < 0
            total_down = day.change + days[index-1].change
            if today_down and yesterday_down and total_down < TradeStrategy2.buy_change_threshold:
                self.keep_stock_day += 1
        elif self.keep_stock_day > 0:
            self.keep_stock_day += 1

    def sell_strategy(self, index, day, days):
        if self.keep_stock_day >= TradeStrategy2.keep_day_threshold:
            self.keep_stock_day = 0

    @classmethod
    def set_keep_day_threshold(cls, keep_day_threshold):
        cls.keep_stock_day = keep_day_threshold

    @classmethod
    def set_buy_change_threshold(cls, buy_change_threshold):
        cls.buy_change_threshold = buy_change_threshold
