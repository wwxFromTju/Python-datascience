#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 索引上的合并
left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                   'value': range(6)})
right1 = DataFrame({'group_val': [3.5, 7]},
                    index=['a', 'b'])
print left1
print right1

# 当连接键位于索引中,可以通过left_index或right_index设置True来指定索引应该被用作连接键
print pd.merge(left1, right1, left_on='key', right_index=True)

# 默认的merge是求取连接键的交集,可以通过外连接获得他们的并集
print pd.merge(left1, right1, left_on='key', right_index=True, how='outer')

# 层次化索引的数据
lefth = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                   'key2': [2000, 2001, 2002, 2001, 2002],
                   'data': np.arange(5.)})
righth = DataFrame(np.arange(12).reshape((6, 2)),
                   index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                          [2001, 2000, 2000, 2000, 2001, 2002]],
                   columns=['event1', 'event2'])
print lefth
print righth
# 面对层次化的索引,用列表的形式指定用于合并键的多个列(注意对于重复索引值的处理):
# 默认忽略掉缺失的值,inner
print pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)
print pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer')

# 同时合并双方的索引
left2 =DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],
                 columns=['Ohio', 'Nevada'])
right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                   index=['b', 'c', 'd', 'e'],
                   columns=['Missouri', 'Alabama'])
print left2
print right2
print pd.merge(left2, right2, left_index=True, right_index=True)
print pd.merge(left2, right2, how='outer', left_index=True, right_index=True)

# join方法, 可以方便地实现按照索引合并。还可以用于合并多个带有相同或者相似索引的DataFrame对象, 而不管他们有没有重叠的列
print left2.join(right2, how='outer')
# 由于历史原因,DataFrame的join方法实在连接键上做左连接。
# 同时支持参数DataFrame的索引和调用者DataFrame的某个列之间的连接
print left1.join(right1, on='key')

# 对于简单的索引合并, 可以向join传入一组DataFrame
another = DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                    index=['a', 'c', 'e', 'f'], columns=['New York', 'Oregon'])
print left2.join([right2, another])

