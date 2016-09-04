#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
# print obj

# 使用drop删除对应的轴上的项
obj_drop = obj.drop('c')
# print obj_drop
obj_drop = obj.drop(['d', 'c'])
# print obj_drop

indexs = ['Ohio', 'Colorado', 'Utha', 'New York']
colunms = ['one', 'two', 'three', 'four']

data = DataFrame(np.arange(16).reshape((4, 4)), index=indexs, columns=colunms)
# print data
# DataFrame对象可以删除任意轴上的索引,包括index和columns
# 如果删除的是index的话,可以不指定axis,这个时候axis默认为0,即为列名
data_drop_index = data.drop(['Colorado', 'Ohio'])
data_drop_index2 = data.drop(['Ohio', 'Utha'], axis=0)
# print data_drop_index
# print data_drop_index2
# 如果删除的是行的话,那么要指定axis=1, 其他与删除列相同
data_drop_columns = data.drop('two', axis=1)
data_drop_columns2 = data.drop(['two', 'four'], axis=1)
# print data_drop_columns
# print data_drop_columns2

# Series的索引值类似于Numpy数组的索引,同时更类似于dict,索引可以不只是数字,可以是字符
obj_series = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
# print obj_series
# 与不同的python不一样,切片的末端是包含的
# python的一般切片等价[] == [)(数学上右边是开)
# 这里的切片[] == [](数学上右边是闭)
# 下面是一般的切片
# print obj_series['b']
# print obj_series[1]
# print obj_series[2:4]
# print obj_series[['b', 'a', 'd']]
# print obj_series[[1,3]]
# print obj_series[obj_series < 2]
# 下面是特殊的末端包含的切片
# obj_series['b':'c'] = 5
# print obj_series


# 对DataFrame的索引就是活的一个或多个列
data = DataFrame(np.arange(16).reshape((4,4)), index=indexs, columns=colunms)
# print data
# print data['two']
# print data[['three', 'one']]
# print data[:2]
# data['three'] > 5 是先获得一个bool的数组,然后通过数组来获得对应的数据
# print data[data['three'] > 5]
# 下面是判断里面的每个值,如果对应的值符合条件,就给予True
# print  data < 5
# 下面是先通过获得一个对应的bool数组,然后对True选出来赋值
data[data < 5] = 0
# print data

# 为了在DataFrame上进行标签索引,使用ix索引字段
# 第一个参数为列,第二个参数为行
# print data.ix['Colorado', ['two', 'three']]
# print data.ix[['Colorado', 'Utah'], [3, 0, 1]]
# print data.ix[2]
# print data.ix[:'Utha', 'two']
# print data.ix[data.three > 5, :3]

# DataFrame常见的索引选项
# obj[val] 选取DataFrame的单个列或一组列, 也可以通过bool数组来过滤行, 行切片, bool型DataFrame
# obj.ix[val] 选择DataFrame的一个行或一组行
# obj.ix[:, val] 选择单个列或者列子集
# obj.ix[val1, val2] 同时选择行和列
# reindex 将一个或者多个轴匹配到新索引上
# xs方法 根据标签选取单行或者单列,并返回一个Series
# icol irow方法 根据整数位置选取单列或单行,并返回一个Series
# get_value set_value 根据行标签和列标签选取单个值