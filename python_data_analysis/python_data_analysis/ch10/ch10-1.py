#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from datetime import datetime, timedelta

now = datetime.now()
# 现在时间
print now
# 现在的年, 月, 日
print '年{}, 月{}, 日{}'.format(now.year, now.month, now.day)

# datetime以毫秒形式储存日期和时间
delta = datetime(2011, 1, 7) - datetime(2011, 1, 5, 23, 30)
print delta
# 对应delta的天数之隔
print delta.days
# 对应delta的秒速之差, 为扣掉天之后
print delta.seconds

start = datetime(2011, 1, 7)
# 加上12天
print start + timedelta(12)
# 减掉24天
print start - 2 * timedelta(12)

# date 以公历形式储存日历日期(年, 月, 日)
# time 将时间储存为时, 分, 秒, 毫秒
# datetime 存储日期和时间
# timedelta 表示datetime值之间的差(日, 秒, 毫秒)