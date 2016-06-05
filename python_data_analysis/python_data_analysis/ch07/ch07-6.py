#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 数据转换
data = DataFrame({'k1': ['one'] * 3 + ['tow'] * 4,
                  'k2': [1, 1, 2, 3, 3, 4, 4]})
print data

# duplicated方法返回一个布尔型Series,表示各行是否重复
print data.duplicated()
# 相应的函数drop_duplicates()方法返回了一个移除了重复行的DataFrame
print data.drop_duplicates()

# 上面的方法默认判断全部的列, 也可以指定部分列进行重复项判断
data['v1'] = range(7)
print data
print data.drop_duplicates(['k1'])

# duplicated drop_duplicates默认是保留第一个出现的值组合。可以传入take_last=True来保留最后一个
print data.drop_duplicates(['k1', 'k2'], take_last=True)
print data.drop_duplicates(['k1', 'k2'], keep='last')
