# encoding=utf-8
import sys
# download from https://github.com/bbfamily/abu
sys.path.append(r'F:\ProgramStudy\Python\abu')
from abupy import ABuSymbolPd
from StockTradeDay import StockTradeDay
from TradeStrategy1 import TradeStrategy1
from TradeLoopBack import TradeLoopBack
import matplotlib.pyplot as plt
import numpy as np

tsla_data = ABuSymbolPd.make_kl_df('TSLA', n_folds=2)
price_array = tsla_data.close.tolist()
date_array = tsla_data.date.tolist()

trade_days = StockTradeDay(price_array, 0, date_array)
trade_loop_back = TradeLoopBack(trade_days, TradeStrategy1())
result = trade_loop_back.execute_trade()

print '回测策略1 总盈亏为：' + str(result) + '%'

plt.plot(np.array(trade_loop_back.profit_array).cumsum())
plt.show()

