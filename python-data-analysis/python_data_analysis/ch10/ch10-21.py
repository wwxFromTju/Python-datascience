#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pytz
from pandas import Series, DataFrame

# 时间序列绘图

# pandas时间绘图功能
close_px_all = pd.read_csv('stock_px.csv', parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px = close_px.resample('B').ffill()
print close_px

# 下面的代码在ipython中运行
# 对其中一列调用plot, 生成简单的图表
close_px['AAPL'].plot()

# 下面代码在ipython中运行
# 对其中的DataFrame调用plot, 所有的时间序列都会被绘制在一个subplot上, 同时会有图例说明
close_px['2009'].plot()

# 下面代码请在ipython中运行
# apple公司在2011年1月到3月的每日股票
close_px['AAPL'].ix['01-2011': '03-2011'].plot()

# 下面代码请在ipython中运行
# 季度型频率的数据会用季度标记进行格式化
# 会按你的拖拉的效果自动进行区间的改变
appl_q = close_px['AAPL'].resample('Q-DEC').ffill()
appl_q.ix['2009':].plot()
