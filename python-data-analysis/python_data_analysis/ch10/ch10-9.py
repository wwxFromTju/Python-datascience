#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pytz
from pandas import Series, DataFrame
from pandas.tseries.offsets import Hour

# 操作时区意识型Timestamp对象
# Timestamp对象可以从单纯型(naive)本地化为时区意识型(time zone-aware)
# 并从一个时区转换到另外一个时区

stamp = pd.Timestamp('2011-03-12 04:00')
stamp_utc = stamp.tz_localize('utc')
print stamp_utc.tz_convert('US/Eastern')

# 在创建Timestamp时, 可以传入一个时区信息
stamp_moscow = pd.Timestamp('2011-03-12 04:00', tz='Europe/Moscow')
print stamp_moscow

# Timestamp对象在内部保存了一个UTC时间戳(UNIX 1970/1/1算起的纳米数), 和时区没有关系
print stamp_utc.value
print stamp_utc.tz_convert('US/Eastern').value

# 使用pandas的DateOffset对象执行时间算术运算时候, 运算过程会自动关注时候存在夏令时转变期
stamp = pd.Timestamp('2012-03-12 01:30', tz='US/Eastern')
print stamp
print stamp + Hour()

# 夏令时转变前90分钟
stamp = pd.Timestamp('2012-11-04 00:30', tz='US/Eastern')
print stamp
# 转变时间
print stamp + 2 * Hour()



