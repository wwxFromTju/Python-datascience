#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 带有重复索引的时间序列

# 在某些运用场景中观测数据可能会落在同一个时间点上
dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000', '1/3/2000'])
dup_ts = Series(np.arange(5), index=dates)
print dup_ts

# 通过检查索引的is_unique属性可以判断是否惟一
print dup_ts.index.is_unique

# 对时间序列进行索引要么为惟一的标量值, 要么为切片
# 标量, 惟一
print dup_ts['1/3/2000']
# 时间切片, 不唯一
print dup_ts['1/2/2000']

# 使用groupby对非惟一时间戳进行聚合, 同时设置level=0
grouped = dup_ts.groupby(level=0)
print grouped.mean()
print grouped.count()

