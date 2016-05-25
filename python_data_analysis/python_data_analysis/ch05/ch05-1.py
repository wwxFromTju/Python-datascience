#!/usr/bin/env python
# encoding=utf-8

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

obj = Series([4, 7, -5, 3])
#  一个带有数据标签的数组,默认是0...n对应相应的数据
# 输出数据标签和对应的数字,最后是数据的类型
# print obj
# 输出数组的所有值
# print obj.values
# 输出数组下标的范围
# print obj.index

# index指定对应的数据标签
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
# print obj2
# print obj2.index
# 通过标签直接操作数据
# 直接通过数组下标访问对应的数据,类似字典
# print obj2['a']
# 通过数据标签来赋值
obj2['d'] = 6
# 通过数据标签的list来指定要访问的数据标签
# print obj2[['c', 'a', 'd']]
# []中间可以加上条件来直接筛选
# print obj2[obj2 > 0]
# 元素级别的操作
# print obj2 * 2
# print np.exp(obj2)
# 判断是否数据标签是否在对应series中
# print 'b' in obj2
# print 'e' in obj2

# 通过字典创建series
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# print sdata
obj3 = Series(sdata)
# 注意数据标签的值是有序的
# print obj3

# 用dict和list创建Series
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, states)
print obj4

