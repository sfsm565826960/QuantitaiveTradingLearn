# encoding=utf-8
import sys
import matplotlib.pyplot as plt
import numpy as np
# download from https://github.com/bbfamily/abu
sys.path.append(r'F:\ProgramStudy\Python\abu')
from abupy import ABuSymbolPd
from StockTradeDay import StockTradeDay
from TradeLoopBack import TradeLoopBack
from TradeStrategy1 import TradeStrategy1
from TradeStrategy2 import TradeStrategy2


tsla_data = ABuSymbolPd.make_kl_df('TSLA', n_folds=2)
price_array = tsla_data.close.tolist()
date_array = tsla_data.date.tolist()
trade_days = StockTradeDay(price_array, 0, date_array)

ts1 = TradeStrategy1()

ts2 = TradeStrategy2()
ts2.set_buy_change_threshold(-0.08)
ts2.set_keep_day_threshold(20)

trade_loop_back = TradeLoopBack(trade_days, ts1)
result = trade_loop_back.execute_trade()

print '回测策略2 总盈亏为：' + str(result) + '%'

plt.plot(np.array(trade_loop_back.profit_array).cumsum())
plt.show()

