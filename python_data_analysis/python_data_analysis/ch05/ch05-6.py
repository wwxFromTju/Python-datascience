#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# 算术运算和数据对齐
# pandas中对不同索引进行计算算术计算。比如算术相加时,结果是索引的并集,各项索引相加,只有一者有的索引是NaN

# Series中的对齐
s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
# print s1
# print s2
# 2者的对称差的索引是NaN
s1_add_s2 = s1 + s2
# print s1_add_s2

# DataFrame的对齐
# 效果和Series一样,不过是同时对齐行和列
df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', "Colorado"])
df2 = DataFrame(np.arange(12.).reshape((4,3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# print df1
# print df2
df1_add_df2 = df1 + df2
# print df1_add_df2

# 填充默认值代替没有出现的值来参与计算
df1_default = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2_defaule = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
# 没有默认值
df1_add_df2_without = df1_default + df2_defaule
# 设置默认值,没有的值来参与计算
df1_add_df2_default = df1_default.add(df2_defaule, fill_value=0)
# print df1_add_df2_without
# print df1_add_df2_default

# 对应的算法方法
# add 加法
# sub 减法
# div 除法
# mul 乘法

# DataFrame 和 Series 之间的计算
arr = np.arange(12.).reshape((3, 4))
# broadcasting广播计算
# print arr - arr[0]
# DataFrame 与 Series之间的计算与broadcast类似
frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series_0 = frame.ix[0]
series_1 = frame.ix[1]
# print frame
# print series_0
# print series_1
# 从第一列开始向下广播,注意列是对应的
# print frame - series_0
# print frame - series_1
# 如果列不是对应的,列属性的对称差为NaN
series2_columns = Series(range(3), index=['b', 'e', 'f'])
# print frame + series2_columns
# 在列上面广播,而不是在行上面广播
series2_index = frame['d']
# print frame
# print series2_index
# 下面的示范是错的,只会将原来index的属性加到columns上,然后全部为NaN
# print frame + series2_index
# 需要明确指定匹配的轴,默认为1
# print frame.sub(series2_index, axis=0)