#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from pandas.tseries.offsets import Hour, Minute

# 频率和日期便宜量
# pandas中的频率通常是由 基础频率 base frequency 和一个乘数组成
# 基础频率通常用字符串别名组成 M : 月, H : 小时等
# 对于每个基础频率, 有对应的日期偏移量 date offset对应对应

# 比如小时的评率对应的Hour类
hour = Hour()
print hour

# 指定偏移量的倍数
four_hours = Hour(4)
print four_hours

# 可以直接通过'H', '4H'等这样的字符串别名直接指定, 在基础频率前放上一个整数即可创建倍数
print pd.date_range('1/1/2000', '1/3/2000 23:59', freq='4h')

# 可以连接偏移量对象
print Hour(2) + Minute(30)

# 也可以直接通过复合的字符串
print pd.date_range('1/1/2000', periods=10, freq='1h30min')

# 对于有些时间点并不是均匀分隔的,比如 'M'月末, 'BM'每月最后一个工作日
# 对于类似的术语, 我们采用锚点偏移量(anchored offset)
# 以下是pandas的评率代码和日期偏移量
# 别名            偏移类型                说明
# D               Day                   每日历日
# B               BusinessDay           每工作日
# H               Hour                  每小时
# T或min          Minute                每分
# S               Second                每秒
# L或ms           Milli                 每毫秒(1/1000)
# U               Micro                 每微秒(1/1,000,000)
# M               MonthEnd              每月最后一个日历日
# BM              BusinessMonthEnd      每月最后一个工作日
# MS              MonthBegin            每月的第一个日历日
# BMS             BusinessMonthBegin    每月的第一个工作日
# W-MON, W-TUE...         Week          指定的星期几(MON, TUE, WED, THU, FRI, SAT, SUN)开始算, 每周
# WOM-1MON, WOM-2MON...   WeekOfMonth   每月的第一个, 第二个, 第三或者第四周的星期几。 例如, WOM-3FRI表示每个月的第三个星期五
# Q-JAN, Q-FRB...         QuarterEnd    对于指定月份(JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC)
#                                       结束的年度, 每季度最后一月的最后一个日历日
# BQ-JAN, BQ-FEB...       BusinessQuarterEnd    对于以指定月份结束的年度, 每季度最后一月的最后一个工作日
# QS-JAN, QS-FEB...       QuarterBegin          对于以指定月份结束的年度, 每季度最后一月的第一个日历日
# BQS-JAB, BQS-FEB...     BusinessQuarterBegin  对于以指定月份结束的年度, 每季度最后一月的第一个工作日
# A-JAN, A-FEB...         YearEnd               每年指定月份(JAN, FEB, MAR, APR, MAY,
#                                               JUN, JUL, AUG, SEP, OCT, NOV, DEC)的最后一个日历日
# BA-JAN, BA-FEB...       BusinessYearEnd       每年指定月份的最后一个工作日
# AS-JAN, AS-FEB...       YearBegin             每年指定月份的第一个日历日
# BAS-JAN, BAS-FEB...     BusinessYearBegin     每年指定月份的第一个工作日


# WOM: Week Of Month
# 每月的第三个周五
rng = pd.date_range('1/1/2012', '9/1/2012', freq='WOM-3FRI')
print list(rng)
