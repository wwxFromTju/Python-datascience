#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pytz
from pandas import Series, DataFrame

# 通过数组创建PeriodIndex

# 固定频率的数据集,通常会将时间信息分开存放在多个列中。
# 比如宏观经济数据集中, 年度和季度就分开存放在不同的列中
data = pd.read_csv('macrodata.csv')
print data.year
print data.quarter

# 将这两个数组以及一个频率传入PeriodIndex,可以合并成DataFrame的一个索引
index = pd.PeriodIndex(year=data.year, quarter=data.quarter, freq='Q-DEC')
print index

data.index = index
print data.infl5





