#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

people = DataFrame(np.random.randn(5, 5),
                   columns=['a', 'b', 'c', 'd', 'e'],
                   index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
print people
people.ix[2:3, ['b', 'c']] = np.nan
print people

mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f': 'orange'}
# 使用字典来转换相应分组
by_column = people.groupby(mapping, axis=1)
print by_column.sum()

# 对于Series可以看成固定大小的索引
map_series = Series(mapping)
print map_series
print people.groupby(map_series, axis=1).count()


# 通过函数进行分组,以返回的值进行分组的依据
print people.groupby(len).sum()

# 混合使用分组依据
key_list = ['one', 'one', 'one', 'two', 'two']
print people.groupby([len, key_list]).min()
