#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from scipy.stats import percentileofscore

# 用户定义的移动窗口函数
# rolling_apply函数使你能够在移动窗口上应用自己设计的数组函数
# 要求: 该函数能从数据的各个片段中产生单个值(即: 约简)
# 比如使用rolling_quantile计算样本分位数时, 可以使用scipy.stats.percentileofscore函数
close_px_all = pd.read_csv('stock_px.csv', parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px = close_px.resample('B').ffill()
returns = close_px.pct_change()

score_at_2percent = lambda x: percentileofscore(x, 0.02)
result = pd.rolling_apply(returns.AAPL, 250, score_at_2percent)
result.plot()
