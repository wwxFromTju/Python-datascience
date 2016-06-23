#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pytz
from pandas import Series, DataFrame

# 时期的频率转换

# Period和PeriodIndex对象可以通过其asfreq方法转换成别的频率

# 将一个年度时期转换为当年年初或年末的一个月度时期
p = pd.Period('2007', freq='A-DEC')
# 转换为第一个月和最后一个月
print p.asfreq('M', how='start')
print p.asfreq('M', how='end')

# 对于不以12月结束的财政年度, 月度子时期的归属情况不一样
p = pd.Period('2007', freq='A-JUN')
# 注意在书上这里错误了
print p.asfreq('M', 'start')
print p.asfreq('M', 'end')

# 将高频率转换为低频率, 超时期(superperiod) 是由子时期(subperiod)所属的位置决定的
# 比如A-JUN频率中, 月份2007-8实际是属于周期2008年的
p = pd.Period('2007-08', 'M')
print p.asfreq('A-JUN')

# PeriodIndex或TimeSeries的频率转换方式
rng = pd.period_range('2006', '2009', freq='A-DEC')
ts = Series(np.random.randn(len(rng)), index=rng)
print ts
print ts.asfreq('M', how='start')
print ts.asfreq('B', how='end')
