#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pandas.io.data as web
from pandas import Series, DataFrame

# 计算来自Yahoo!Finance的股票价格和成交量

all_data = {}
# 通过pandas来获得对应时间段内的公司的交易的数据
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')
price = DataFrame({tic: data['Adj Close'] for tic, data in all_data.iteritems()})
volume = DataFrame({tic: data['Volume'] for tic, data in all_data.iteritems()})

# 计算价格白枫树
