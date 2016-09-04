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

# 在列列连接的时候,DataFrame对象的索引会被丢弃

# 对于都有的列名,且没有拿去合并,这样保留下来容易混乱
print pd.merge(left, right, on='key1')
# 通过suffixes来显式指定新的列名
print pd.merge(left, right, on='key1', suffixes=('_left', '_right'))

print pd.merge(left=left, right=right,left_on='key1', right_on='key1')

print pd.merge(left, right, left_index=True, on='key1')

print pd.merge(left, right, right_index=True, on='key1')

# left 参与合并左侧的DataFrame
# right 参与合并右侧的DataFrame
# how 有参数 inner, outer, left, right, 默认为inner
# on 指定用于连接的列名, 必须存在左右2个DataFrame对象中。如果没有指定,且其他连接键也没有指定,则以left和right列名的交集作为连接键
# left_on 左侧DataFrame中用于连接键的列
# right_on 右侧DataFrame中用于连接键的列
# left_index 将左侧的行索引用于其连接键
# right_index 将右侧的行索引用于其连接键
# sort 默认为True,, 根据连接键对合并后的数据进行排序。大量数据建议False
# suffixes 字符串元组,用于追加到重叠列名的末尾, 默认为('_x', '_y'), 如左右两边都出现'data',而且key中没有'data',则会出现'data_x','data_y'
# copy 默认为False, 可以在某些特殊情况下避免将数据复制到结果数据结构中。默认是总是复制
