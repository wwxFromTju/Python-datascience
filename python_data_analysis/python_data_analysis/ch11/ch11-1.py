#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 金融和经济数据应用

# 截面cross-section 用来表示某个时间点的数据,比如标准普尔500指数中所有成分股在特定日期的收盘价就会形成一个截面
# 面板panel 用来表示多个数据项(例如价格和成交量)在多个时间点的截面数据

# 数据对齐data alignment
# 处理价格
prices = pd.read_csv('stock_px.csv', index_col=0, sep=',')
cols = ['AAPL', 'JNJ', 'SPX', 'XOM']
prices = prices.loc['2011-09-06':'2011-09-15', cols]
print prices

volume = pd.read_csv('volume.csv', index_col=0, sep=',')
cols = ['AAPL', 'JNJ', 'XOM']
volume = volume.loc['2011-09-06':'2011-09-13', cols]
print volume

# 计算成交量加权平均价格
# pandas会自动将数据对齐
print prices * volume
# 类似sum函数会将NaN值排除
vwap = (prices * volume).sum() / volume.sum()
print vwap
print vwap.dropna()

# 手工对齐
print prices.align(volume, join='inner')

# 通过一组索引可能不同的Series构建DataFrame
s1 = Series(range(3), index=['a', 'b', 'c'])
s2 = Series(range(4), index=['d', 'b', 'c', 'e'])
s3 = Series(range(3), index=['f', 'a', 'c'])
print DataFrame({'one': s1, 'two': s2, 'three': s3})
# 丢弃索引
print DataFrame({'one': s1, 'two': s2, 'three': s3}, index=list('face'))
