#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from datetime import datetime

# 日期的范围, 评率以及移动
# 对于数据通常在一定评率范围内进行研究, 比如每日, 每月, 每15mins等, 这样会引入相应的缺失值
# pandas中有直接一套标准进行重采样,评率推断, 生成固定评率日期

# 最基本的时间序列: 以时间戳为索引的Series
dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7),
         datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]

ts = Series(np.random.randn(6), index=dates)
print ts

# 重采样
print ts.resample('D')

# 指定生成日期范围
index = pd.date_range('4/1/2012', '6/1/2012')
print index

# 如果只指定开始或者结束时间点,那么需要再指定日期范围
print pd.date_range(start='4/1/2012', periods=20)
print pd.date_range(end='6/1/2012', periods=20)
print pd.date_range(start='4/1/2012', end='6/1/2012')

# 如果需要产生像每个月最后一个工作日组成的索引, 那么可以传入'BM'评率(business end of month)
print pd.date_range('1/1/2000', '12/1/2000', freq='BM')

# date_range会默认保留起始和结束时间戳的时间信息
print pd.date_range('5/2/2012 12:56:31', periods=5)

# 规范化(normalize)到午夜时间的时间戳,
print pd.date_range('5/2/2012 12:56:31', periods=5, normalize=True)

