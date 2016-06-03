#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as py
from pandas import Series, DataFrame

# 合并数据集

key = ['b', 'b', 'a', 'c', 'a', 'a', 'b']
key2 = ['a', 'b', 'd']

# merge/join
df = DataFrame({'key': key,
                'data1': range(7)})
df2 = DataFrame({'key': key2,
                 'data2': range(3)})
print df
print df2
# 如果没有指定合并的列名,则merge会将重叠列的列名当做键来合并
# 多对一
print pd.merge(df, df2)
# 明显指定合并的列名
print pd.merge(df, df2, on='key')

df3 = DataFrame({'lkey': key,
                 'data1': range(7)})
df4 = DataFrame({'rkey': key2,
                 'data2': range(3)})
# 当左右要合并的列名不一样时,可以显式指定
print pd.merge(df3, df4, left_on='lkey', right_on='rkey')

# 上面的merge默认的是'inner',所以结果的键是交集,所以没有c,d
# 可以通过how指定连接方法
# 外连
print pd.merge(df, df2, how='outer')

# 多对多
df_many = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                     'data1': range(6)})
df2_many = DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                      'data2': range(5)})

# 多对多连接产生的行是笛卡尔积
# left 则左边全部,右边可以为NaN
print pd.merge(df_many, df2_many, on='key', how='left')

# 多个键合并,传入一个由列名组成的列表即可
left = DataFrame({'key1': ['foo', 'foo', 'bar'],
                  'key2': ['one', 'two', 'one'],
                  'lval': [1, 2, 3]})
right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                   'key2': ['one', 'one', 'one', 'two'],
                   'rval': [4, 5, 6, 7]})
# 在on中通过list指定多个key合并
print pd.merge(left, right, on=['key1', 'key2'], how='outer')
