#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pytz
from pandas import Series, DataFrame

# 将Timestamp转换为Period(及反向过程)

# 使用to_period方法, 可以将时间戳索引的Series, DataFrame对象转换成以时期索引
rng = pd.date_range('1/1/2000', periods=3, freq='M')
ts = Series(np.random.randn(3), index=rng)
print ts
pts = ts.to_period()
print pts

# 由于时期指定的是非重叠时间区间, 对于给定的频率,一个时间戳只能属于一个时期
# 信PeriodIndex的频率默认是重时间戳推断而来的, 结果中允许重复时期
rng = pd.date_range('1/29/2000', periods=6, freq='D')
ts2 = Series(np.random.randn(len(rng)), index=rng)
print ts2.to_period('M')

# 转换为时间戳, 使用to_timestamp
pts = ts.to_period()
print pts
print pts.to_timestamp(how='end')
