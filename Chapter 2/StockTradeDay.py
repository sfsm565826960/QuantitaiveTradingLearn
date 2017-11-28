# encoding=utf-8
from collections import namedtuple, OrderedDict


class StockTradeDay(object):
    """
    股票对象，包含日期、价格、变化\
    :param price_array: 价格数值，要求float或可转为float的字符串
    :param start_date: 开始日期，要求为可转为int的数值，如20171128
    :param date_array: 【可选】指定日期数组,指定后start_date无效
    """
    def __init__(self, price_array, start_date, date_array = None):
        self.__price_array = [float(price) for price in price_array]
        self.__date_array = self._init_date(start_date, date_array)
        self.__diff_array, self.__change_array = self.__init_diff_and_change()
        self.stock_dict = self._init_stock_dict()

    def _init_date(self, start_date, date_array = None):
        """
        初始化日期
        :param start_date: 开始日期，要求为数值或可转为数值的字符串
        :param date_array: 【可选】指定日期数组
        :return: date_array, dtype为str
        """
        if date_array is None:
            try:
                start_date = int(start_date)
            except ValueError as e:
                raise TypeError('start_date[{}, {}] cannot covert to int.'.format(
                    type(start_date), start_date))
            date_array = [str(start_date + index)
                          for index, _ in enumerate(self.__price_array)]
        else:
            date_array = [str(date) for date in date_array]
        return date_array

    def __init_diff_and_change(self):
        pp_array = [(price1, price2) for price1, price2 in zip(
            self.__price_array[:-1], self.__price_array[1:])]
        diff_array = map(lambda pp: reduce(lambda p1, p2: p2 - p1, pp), pp_array)
        diff_array.insert(0, 0)
        change_array = map(lambda pp: reduce(
            lambda p1, p2: round((p2 - p1) / p1, 2), pp), pp_array)
        change_array.insert(0, 0)
        return diff_array, change_array

    def _init_stock_dict(self):
        stock_namedtuple = namedtuple('stock', ('date', 'price', 'diff','change'))
        stock_ordered_dict = OrderedDict(
            (date, stock_namedtuple(date, price, diff, change))
            for date, price, diff, change in
            zip(self.__date_array, self.__price_array, self.__diff_array, self.__change_array))
        return stock_ordered_dict

    def filter_stock(self, want_up=True, want_calc_sum=False):
        """
        筛选股票
        :param want_up: 是否筛选上涨，默认True，下跌False
        :param want_calc_sum: 是否计算涨跌幅，默认False
        :return stock_array | float
        """
        filter_func = (lambda stock: stock.change > 0) if want_up else (lambda stock: stock.change < 0)
        filter_stock = filter(filter_func, self.stock_dict.values())
        if want_calc_sum:
            change_sum = 0
            for stock in filter_stock:
                change_sum += stock.change
            return change_sum
        else:
            return filter_stock

    def __len__(self):
        return len(self.__price_array)

    def __getitem__(self, index):
        date_key = self.__date_array[index]
        return self.stock_dict[date_key]

    def __iter__(self):
        for date_key in self.stock_dict:
            yield self.stock_dict[date_key]

    def __str__(self):
        return str(self.stock_dict)
    __repr__ = __str__


if __name__ == '__main__':
    # 测试用
    _price_array = ['30.14', '29.58', '26.36', '32.56', '32.82']
    _start_date = '20170118'

    _std = StockTradeDay(_price_array, _start_date)

    print _std

    print _std.filter_stock()
    print _std.filter_stock(False, True)