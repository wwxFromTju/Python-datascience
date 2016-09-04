#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 二元移动窗口函数

close_px_all = pd.read_csv('stock_px.csv', parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px = close_px.resample('B').ffill()

# 有些统计运算需要在两个时间序列上执行
# 比如某只股票对某个参考指数(比如标准普尔500指数)的相关系数感兴趣
spx_px = close_px_all['SPX']
spx_rets = spx_px / spx_px.shift(1) -1
returns = close_px.pct_change()
corr = pd.rolling_corr(returns.AAPL, spx_rets, 125, min_periods=100)
# 注意一下下面的代码在ipython中运行
corr.plot()

# 一次性计算多只股票与标准普尔500指数的相关系数
# 传入一个TimeSeries和一个DataFrame各列的相关系数
corr = pd.rolling_corr(returns, spx_rets, 125, min_periods=100)
# 下面的代码需要在ipython中运行
corr.plot()


