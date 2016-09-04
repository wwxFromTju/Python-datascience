#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pytz
from pandas import Series, DataFrame

# 按季度计算的时间频率
# 季度型数据在会计和金融等领域中很常见

# '财年末': 通常一年12个月中某月的最后一个日历日或者工作日
# 所以2012Q4 会根据财年末的不同会有不同的含义, pandans有12种季度性频率, 从Q-JAN到Q-DEC
p = pd.Period('2012Q4', freq='Q-JAN')
print p

# 以一月结束的财年中, 2012Q4是从11月到1月
print p.asfreq('D', 'start')
print p.asfreq('D', 'end')

# 获取该季度倒数第二个工作日下午4点的时间戳
# 第一个asfreq是找到最后一个工作日,然后前一天
# 然后第二个asfreq是转换为分钟的开始,然后加到对应的时间点
p_4pm = (p.asfreq('B', 'e') - 1).asfreq('T', 's') + 16 * 60
print p_4pm
print p_4pm.to_timestamp()

# period_range可以用来生成季度型范围
rng = pd.period_range('2011Q3', '2012Q4', freq='Q-JAN')
ts = Series(np.arange(len(rng)), index=rng)
print ts

# 注意是工作日
new_rng = (rng.asfreq('B', 'e') - 1).asfreq('T', 's') + 16 * 60
ts.index = new_rng.to_timestamp()
print ts

