#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from datetime import time
from pandas import Series, DataFrame

# 时间和'最当前'数据选取
# 对于长时间市场数据,选取每天特定时间的价格数据
# 对于数据不规整, 要数据规整
rng = pd.date_range('2012-06-01 09:30', '2012-06-06 15:59', freq='T')
ts = Series(np.arange(len(rng), dtype=float), index=rng)
print ts

# 十点
print ts[time(10, 0)]
# 等价于
# 可以使用实例方法at_time
print ts.at_time(time(10, 0))

# 选取两个Time对象之间的值
# 选取10:00到10:01之间
print ts.between_time(time(10, 0), time(10, 1))

# 得到上午10之前最后出现的那个值
indexer = np.sort(np.random.permutation(len(ts))[700:])
irr_ts = ts.copy()
irr_ts[indexer] = np.nan
print irr_ts['2012-06-01 09:50': '2012-06-01 10:00']

# 如果将一组Timestamp传入asof方法, 就可以得到这些时间点处的有效值(非NA)
selection = pd.date_range('2012-06-01 10:00', periods=4, freq='B')
print irr_ts.asof(selection)




