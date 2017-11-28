# encoding=utf-8

from six import add_metaclass
from abc import ABCMeta, abstractmethod


@add_metaclass(ABCMeta)
class TradeStrategyBase(object):
    """
    交易策略抽象基类
    """

    @abstractmethod
    def buy_strategy(self, *args, **kwargs):
        """
        买入策略基类
        :param args:
        :param kwargs:
        :return:
        """

    @abstractmethod
    def sell_strategy(self, *args, **kwargs):
        """
        卖出策略基类
        :param args:
        :param kwargs:
        :return:
        """


if __name__ == '__main__':
    # 测试用
    class TradeStrategy1(TradeStrategyBase):
        def buy_strategy(self, *args, **kwargs):
            print 'buy'
            print args
            print kwargs

        def sell_strategy(self, *args, **kwargs):
            print 'sell'
            print args
            print kwargs

    ts1 = TradeStrategy1()
    ts1.buy_strategy('1', k='buy')
    ts1.sell_strategy('2', k='sell')