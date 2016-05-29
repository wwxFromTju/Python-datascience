#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pandas.io.data as web
# from pandas.datareader import web
from pandas import Series, DataFrame

# 计算来自Yahoo!Finance的股票价格和成交量

all_data = {}
# 通过pandas来获得对应时间段内的公司的交易的数据
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')
price = DataFrame({tic: data['Adj Close'] for tic, data in all_data.iteritems()})
volume = DataFrame({tic: data['Volume'] for tic, data in all_data.iteritems()})

# 计算价格百分数变化
returns = price.pct_change()
# print returns.tail()

# series的corr方法用于计算两个series中重叠的,非NA的,按索引对齐的值的相关系数
# print returns.MSFT.corr(returns.IBM)
# cov 用与计算协方差
# print returns.MSFT.cov(returns.IBM)

# 对DataFrame就是直接统计各列间的如:相关系数,协方差等等
# print returns.corr()
# print returns.cov()

# 利用DataFrame的corrwith可以计算列或者行和另外一个Series或者DataFrame之间的相关系数
# print returns.corrwith(returns.IBM)
# 传入为DataFrame则会按照列名配对
# print returns.corrwith(volume)
