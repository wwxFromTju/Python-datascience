#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pytz
from pandas import Series, DataFrame

# 时期及其算术运算
# 时期(period)表示的时间区间, 比如数日...
# Period类所表示的就是上述的数据类型, 构造函数需要一个字符串或整数, 以及相应的频率

# 表示2007/1/1到2007/12/31之间的整段时间
p = pd.Period(2007, freq='A-DEC')
print p

# 加上数字是按照频率进行位移的
# 按年移动
print p + 5
print p - 2

# 如果频率一样, 那么差就是之间的单位数量
print pd.Period('2014', freq='A-DEC') - p

# 创建规则的时间范围
rng = pd.period_range('1/1/2000', '6/30/2000', freq='M')
print rng

# PeriodIndex类保存了一组Period, 它可以在任何的pandas数据结构中用作轴索引
print Series(np.random.randn(6), index=rng)

# PeriodIndex类的构造函数允许使用一组字符串
values = ['2001Q3', '2002Q2', '2003Q1']
index = pd.PeriodIndex(values, freq='Q-DEC')
print index
