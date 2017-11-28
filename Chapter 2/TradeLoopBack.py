# encoding=utf-8


class TradeLoopBack(object):
    """
    交易回测系统
    :param trade_days:
    :param trade_strategy:
    """
    def __init__(self, trade_days, trade_strategy):
        self.trade_days = trade_days
        self.trade_strategy = trade_strategy
        self.profit_array = [] # 交易盈亏结果序列

    def execute_trade(self):
        """
        执行交易回测
        :return:
        """
        for index, day in enumerate(self.trade_days):
            if hasattr(self.trade_strategy, 'keep_stock_day') \
                    and self.trade_strategy.keep_stock_day > 0: # 如果持有股票
                self.profit_array.append(day.change) # 添加当日盈亏

            if hasattr(self.trade_strategy, 'buy_strategy'):
                self.trade_strategy.buy_strategy(index, day, self.trade_days)

            if hasattr(self.trade_strategy, 'sell_strategy'):
                self.trade_strategy.sell_strategy(index, day, self.trade_days)

        return reduce(lambda p1, p2: p1 + p2, self.profit_array) * 100
