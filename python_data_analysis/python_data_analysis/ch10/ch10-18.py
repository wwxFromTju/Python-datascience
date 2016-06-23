#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pytz
from pandas import Series, DataFrame

# OHLC重采样
# 金融领域中通常计算面元的4个值: 第一个值 open 开盘, 最后一个值 close 收盘, 最大值 high 最高, 最小值 low 最低

rng = pd.date_range('1/1/2000', periods=12, freq='T')
ts = Series(np.arange(12), index=rng)

# 传入how='ohlc' 可以得到计算上面4个聚合值的DataFrame
# 下面的Future未来可能会被抛弃
# print ts.resample('5min', how='ohlc')
# 下面是正在使用的方法
print ts.resample('5min').ohlc()

# 使用groupby来实现降采样
rng = pd.date_range('1/1/2000', periods=100, freq='D')
ts = Series(np.arange(100), index=rng)
print ts.groupby(lambda x: x.month).mean()
print ts.groupby(lambda x: x.weekday).mean()
