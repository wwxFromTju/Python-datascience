#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pytz
from pandas import Series, DataFrame

# 降采样
# 将数据聚合到规整的低频率

# '1分钟'数据
# 下面是12分钟
rng = pd.date_range('1/1/2000', periods=12, freq='T')
ts = Series(np.arange(12), index=rng)
print ts

# 聚合到5分钟中
print ts.resample('5min').sum()
# 设置对应的面元边界, 就是区间的边界
print ts.resample('5min', closed='left').sum()
print ts.resample('5min', closed='right').sum()

# 最终的时间序列是以各面元右边界的时间戳进行表示的,可以通过label来设置
print ts.resample('5min', closed='left', label='left').sum()

# 通过loffset设置偏移
print ts.resample('5min', loffset='-1s').sum()
# 等价于shift
print ts.resample('5min').shift(-1).sum()
