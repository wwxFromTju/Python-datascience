#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from datetime import datetime
from pandas.tseries.offsets import Day, MonthEnd

# 移动(超前/滞后)数据
# 移动 shifting : 将时间前移或者后移

# Series和DataFrame都有一个对应的shift方法用于执行单纯的前移或者后移,同时保持索引不变
ts = Series(np.random.randn(4), index=pd.date_range('1/1/2000', periods=4, freq='M'))
print ts
# 向后移动
print ts.shift(2)
# 向前移动
print ts.shift(-2)

# 通常是用shift来计算一个时间序列或者多个时间序列中百分比的变化
print ts / ts.shift(1) - 1

# 只是移动shift并不会修改索引, 可以指定频率来对时间戳移动, 而不是移动数据,然后产生NaN
print ts.shift(2, freq='M')
print ts.shift(3, freq='D')
print ts.shift(1, freq='3D')
print ts.shift(1, freq='90T')

# 通过偏移量对日期进行位移
now = datetime(2011, 11, 17)
print now + 3 * Day()

# 可以加锚点偏移量, 比如MonthEnd, 在第一次会将原日期前滚(未来)到符合频率规则的下一个日期
print now + MonthEnd()
print now + MonthEnd(2)

# 对于锚点偏移量的rollforward和rollback方法,可以直接指定前滚(未来)/后滚(以前)
offset = MonthEnd()
# 前滚
print offset.rollforward(now)
# 后滚
print offset.rollback(now)

# 可以结合groupby使用这两个滚动方法
ts = Series(np.random.randn(20), index=pd.date_range('1/15/2000', periods=20, freq='4d'))
print ts.groupby(offset.rollforward).mean()
# 等价于
print ts.resample('M', how='mean')

