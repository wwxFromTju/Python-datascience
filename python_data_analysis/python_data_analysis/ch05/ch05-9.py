#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 汇总和计算描述统计
# pandas的汇总和计算是基于没有缺失数据的假设的
# 主要是对于Series来进行sum或者其他的统计,或者DataFrame来进行行或者列的计算,返回对应的Series

df = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
               index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
# print df
# 对于列进行统计,忽略掉NaN
# print df.sum()
# 对于行进行统计,忽略掉NaN
# print df.sum(axis=1)
# 可以显式指定:不忽略NaN,一旦有NaN,则结果为NaN
# print df.mean(axis=1, skipna=False)

# 约简方法
# axis 指定轴,行用0, 列用1, 默认为0
# skipna 默认True,忽略NaN
# level 如果轴是层次化索引的(即:MultiIndex),根据level分组化简

# 有些方法是间接统计, 即返回的值是对应的索引的值
# idxmax 统计各列, 判断列的属性在那个index中最大, 第一个值为colunms的属性, 第二个值为最大的索引的值
# 类似有idxmim等
# print df.idxmax()

# 累计统计
# 如下, 为依次相加,如果自己属性为NaN,则为NaN,否则忽略前面的NaN,然后全部加起来
# print df.cumsum()

# 也可以一次统计多个汇总统计
# print df.describe()

# 对于非数值型,统计的出现的不同的个数,出现最多的,出现最频繁的次数等等
obj = Series(['a', 'a', 'b', 'c'] * 4)
# print obj
# print obj.describe()
obj2 = Series([1.1, 2, 3] * 10)
# print obj2.argmax()
# print obj2.idxmax()
# print obj2.quantile()
# print obj2.mean()
# print obj2.mad()
# print obj2.var()
# print obj2.std()
# print obj2.skew()
# print obj2.cumsum()
# print obj2.cummin()
# print obj2.cummax()
# print obj2.cumprod()
# print obj2.diff()
# print obj2.pct_change()

# 描述和汇总统计
# count 统计不是NaN的数量
# describe 针对Series,DataFrame列(不可以设置axis)计算汇总统计
# min max 计算最下/最大值
# argmin argmax 计算最小/最大值的索引的位置(只能针对数字, Series)
# idxmin idxmax 计算最小/最大值得索引值(针对数字)
# quantile 计算分位数
# sum 值的总和
# mean 值的平均数
# median 值的算术中位数
# mad 根据平均值计算平均绝对离差
# var 计算样本方差
# std 计算样本标准差
# skew 计算样本值的偏度(三阶矩?)
# kurt 计算样本值的峰度(四阶矩?)
# cumsum 样本值的累计和
# cummin cummax 计算累积的最小值 最大值
# cumprod 样本值的累计值
# diff 一阶差分
# pct_change 百分数变化
