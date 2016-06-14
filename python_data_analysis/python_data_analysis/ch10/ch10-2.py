#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from datetime import datetime, timedelta
from dateutil.parser import parse

# 字符串和datetime之间的相互转换
stamp = datetime(2011, 1, 3)
print str(stamp)
# 根据格式,格式化对应的日期
print stamp.strftime('%Y-%m-%d')

# 将字符串转换为datetime
value = '2011-01-03'
print datetime.strptime(value, '%Y-%m-%d')
# year, month, day, hour, minute
print datetime(2011, 1, 3, 0, 0)

datestrs = ['7/6/2011', '8/6/2011']
print [datetime.strptime(x, '%m/%d/%Y') for x in datestrs]

# datetutil可以解析几乎所有人类能够理解的日期表达形式
print parse('2011-01-03')
print parse('Jan 31, 1997, 10:45PM')

# 在国际通用的格式中, 通常日在月前, 可以通过dayfirst来设置
print parse('6/12/2011')
print parse('6/12/2011', dayfirst=True)

# to_datetime可以解析多种不同的日期表示形式
datestrs_diff = ['7/6/2011', '8/6/2011', 'Jan 31, 1997, 10:45PM', '2011-01-03']
print datestrs_diff
print pd.to_datetime(datestrs_diff)
# to_datetime可以处理缺失值(None, 空字符串等)
idx = pd.to_datetime(datestrs_diff + [None] + [''])
# 缺失值填充的是NaT: Not a Time
print idx
print pd.isnull(idx)

# datetime格式定义
# %Y 4位数的年
# %y 2位数的年
# %m 2位数的月 01-12
# %d 2位数的日 01-31
# %H 小时(24) 00-23
# %I 小时(12) 01-12
# %M 2位数的分 00-59
# %S 秒 00-61 60,61用于闰秒
# %w 用整数表示的星期几 0-6 0:星期天
# %U 每年的第几周 00-53 星期天为每周的第一天, 每年的第一周的星期一之前的那几天被认为是第0周
# %W 和%U类似, 只是将星期一当做每周的第一天
# %z 以 +HHMM 或 -HHMM 表示的UTC时区的偏移量, 如果时区为naive, 返回空字符串
# %F 等价于%Y-%m-%d 2016-01-01
# %D 等价于%m/%d/%y 01/01/2016

# 一些特定于当前环境的格式化选项
# %a 星期几的简写
# %A 星期几的全称
# %b 月份的简写
# %B 月份的全称
# %c 完整的日期和时间, 例如'Tue 01 May 2016 01:01:01 PM'
# %p 不同环境中的AM或PM
# %x 适合当前环境的日期格式, 例如, 在美国, 'May 1, 2012' -》 05/01/2012
# %X 适合当前环境的时间格式, 例如'04:24:12 PM'









