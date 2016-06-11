#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 用于特定分组的值填充缺失值


s = Series(np.random.randn(6))
s[::2] = np.nan
print s
# 用均值来填充nan值
print s.fillna(s.mean())

states =['Ohio', 'New York', 'Vermont', 'Florida',
         'Oregon', 'Nevada', 'California', 'Idaho']
group_key = ['East'] * 4 + ['West'] * 4
data = Series(np.random.randn(8), index=states)
print data
data[['Vermont', 'Nevada', 'Idaho']] = np.nan
print data
print data.groupby(group_key).mean()

# 用分组平均填充NA值
fill_mean = lambda g: g.fillna(g.mean())
print data.groupby(group_key).apply(fill_mean)

# 预定义分组填充值
fill_values = {'East': 0.5, 'West': -1}
fill_func = lambda g: g.fillna(fill_values[g.name])
print data.groupby(group_key).apply(fill_func)