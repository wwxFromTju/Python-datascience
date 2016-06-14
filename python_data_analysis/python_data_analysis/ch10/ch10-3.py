#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from datetime import datetime

# 时间序列基础

# 最基本的时间序列: 以时间戳为索引的Series
dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7),
         datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]

# 这些datetime对象实际上是被放在一个DatetimeIndex中
# ts视为TimeSeries
# 在现在这个pandas中, 将TimeSeries忽略掉了, 请使用Series, 不要显示使用TimeSeries
ts = Series(np.random.randn(6), index=dates)
print ts
print type(ts)
print ts.index

# 不同索引的时间序列之间的算术运算会自动按照日期对齐
# 没有相应索引的填充NaN
print ts + ts[::2]

# 类型使用Numpy的datetime64数据类型以纳米形式存储时间戳
print ts.index.dtype

# DatetimeIndex中各个标量值是pandas的Timestamp对象
stamp = ts.index[0]
print stamp
