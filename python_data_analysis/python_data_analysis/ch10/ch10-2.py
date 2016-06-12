#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from datetime import datetime, timedelta

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
print [datetime.strptime(x, '%m%d')]