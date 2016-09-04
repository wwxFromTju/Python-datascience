#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 连接concatenation, 绑定binding, 堆叠stacking

# Numpy有一个用于合并原始Numpy数组的concatentation函数
arr = np.arange(12).reshape((3, 4))
print arr
# 即在对应轴的方向合并
print np.concatenate([arr, arr], axis=1)

# 对于没有重叠索引的Series, 就是拼接起来
s1 = Series([0, 1], index=['a', 'b'])
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = Series([5, 6], index=['f', 'g'])
# 默认是在axis=0上面工作的
print pd.concat([s1, s2, s3])
# 指定axis
# 注意:另外一条轴上没有重叠
print pd.concat([s1, s2, s3], axis=1)
# 可以通过join指定inner来选取交集
s4 = pd.concat([s1 * 5, s3])
print s4
print pd.concat([s1, s4], axis=1)
print pd.concat([s1, s4], axis=1, join='inner')

# 可以通过join_axes来指定要在其他轴上面使用的索引
print pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e', 'wwx']])

# 连接的片段可以使用keys来创建层次索引
result = pd.concat([s1, s2, s3], keys=['one', 'two', 'three'])
print result
print result.unstack()

# 如果沿axis=1对Series进行合并, 那么keys会变成DataFrame的列头
print pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'])

df1 = DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                columns=['one', 'two'])
df2 = DataFrame(5 + np.arange(4).reshape(2, 2,), index=['a', 'c'],
                columns=['three', 'four'])
print pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])
# 如果传入的是一个字典,则字典的键会被当成keys选项的值
print pd.concat({'level1': df1, 'level2': df2}, axis=1)

# 可以使用names来为原来的列名和keys命名, 第一个值是keys的name, 第二个值是原来的列名的name
print pd.concat([df1, df2], axis=1, keys=['level1', 'level2'],
                names=['upper', 'lower'])

# 当行索引没有意义时
df1 = DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
print df1
print df2
# 只是拼接下去
print pd.concat([df1, df2], ignore_index=True)

# concat函数的参数
# objs 参与连接的pandas对象的列表或者字典,第一个参数
# axis 指明连接的轴向, 默认为0
# join 'inner' 'outer' 默认为'outer'。outer是并集, inner是交集
# join_axes 用于指明用于其他n-1条轴的缩影,不执行并集/交集运算
# keys 可以形成层次化索引
# levels 用于创建分层级别的名称
# names 用于创建分层级别的names
# verify_integrity 检查结果对象新轴上的重复情况, 如果发现则引发异常。默认是False
# ignore_index 不保留连接轴上的索引,产生一组新索引
