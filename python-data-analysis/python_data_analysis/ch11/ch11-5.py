#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pandas.io.data as web
# from pandas_datareader import data, wb
from pandas import Series, DataFrame

# 收益指数和累计收益
# 收益return 通常是指某资产价格的百分比变化

price = web.get_data_yahoo('AAPL', '2011-01-01', '2012-07-27')['Adj Close']
print price[-5:]

# 计算两个时间点之间的累计百分比回报: 计算价格百分比变化即可
print price['2011-10-03'] / price['2011-3-01'] - 1

# 苹果公司股票的简单的收益指数
returns = price.pct_change()
ret_index = (1 + returns).cumprod()
ret_index[0] = 1
print ret_index

# 计算指定时间内的累计收益
m_returns = ret_index.resample('BM', how='last').pct_change()
print m_returns['2012']

# 通过重采样聚合(聚合的是时期), 从日百分比变化中计算得出
m_rets = (1 + returns).resample('M', how='prod', kind='period') - 1
print m_rets['2012']

# 如果知道股息的派发日和支付率, 那么可以加入每日收益中
# returns[dividend_dates] += dividend_pcts
