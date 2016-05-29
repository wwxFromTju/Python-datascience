#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 唯一值,值计数,成员资格
obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
# unique 可以得到Series中的唯一值的数组,即每个值都只出现一次,将重复出现的忽略成一个
# print obj.unique()
# value_counts 计算一个series中各个值的出现的频率, 默认降序排列
# print obj.value_counts()
# 可以使用pd来直接计算评率
# 不排序?
# print pd.value_counts(obj.values, sort=False)
# 降序
# print pd.value_counts(obj.values, sort=True)
# isin 判断矢量化集合的成员资格,是否在里面
mask = obj.isin(['b', 'c'])
# print mask
# print obj[mask]

# isin 返回一个表示Series各值是否包含与传入的值序列中的布尔型数组
# unique 计算series中的唯一值数组,按发现顺序返回
# value_counts 返回一个Series, 索引为唯一值, 其值为频数, 降序排列

data = DataFrame({'Qu1': [1, 3, 4, 3, 4],
                  'Qu2': [2, 3, 1, 2, 3],
                  'Qu3': [1, 5, 2, 4, 4]})
# print data
result = data.apply(pd.value_counts).fillna(0)
# print result

