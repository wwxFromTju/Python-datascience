#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pytz
from pandas import Series, DataFrame

# 不同时区之间的运算
# 不同时区的运算,最终结果会是UTC
# 时间戳其实是以UTC存储的,所以是一个简单的运算,并不需任何转换

rng = pd.date_range('3/7/2012 9:30', periods=10, freq='B')
ts = Series(np.random.rand(len(rng)), index=rng)
print ts

ts1 = ts[:7].tz_localize('Europe/London')
ts2 = ts[2:].tz_localize('Europe/Moscow')
result = ts1 + ts2
# 输出对应的时间戳
print result.index


