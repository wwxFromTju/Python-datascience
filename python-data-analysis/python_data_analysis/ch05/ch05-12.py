#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 处理缺失数据

# NaN(Not a Number) 表示浮点/非浮点数组中的缺失值
string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])
# print string_data
# print string_data.isnull()
# Python内置的None值也会被当作NA处理
string_data[0] = None
# print string_data.isnull()
# print string_data.dropna()
# print string_data.notnull()

# NA处理办法
# dropna 将不是NA的过滤出来,然后返回,可以通过阈值调节对缺失值的容忍程度
# fillna 在插值的时候或者指定值的时候(如ffill bfill)填充缺失数据
# isnull  返回布尔型数据,是NA的返回True, 不是NA的返回False
# notnull 与isnull相反, 不是NA返回True, 是NA的返回False


# 过滤缺失数据

# 对于Series  dropna返回仅含非空数据和索引值的Series
data_nan = Series([1, np.nan, 3.5, np.nan, 7])
# print data_nan
# print data_nan.dropna()
# 与dropna效果一样,通过布尔数据来筛选出来
# print data_nan[data_nan.notnull()]

# 对于DataFrame对象,dropna筛去所有包含NA的行或列
# dropna默认筛去所有含有np.nan的行
data_nan_dataframe = DataFrame([[1., 6.5, 3.],
                                [1., np.nan, np.nan],
                                [np.nan, np.nan, np.nan],
                                [np.nan, 6.5, 3]])
# print data_nan_dataframe
# 默认删掉所有包含NA的行
# print data_nan_dataframe.dropna()
# all只删掉全部为NA的行
# print data_nan_dataframe.dropna(how='all')
# 可以指定axis
# print data_nan_dataframe.dropna(axis=1)

# 对于时间序列
# 如果只是想留下一部分观测数据, 可以使用thresh参数来实现目的
data_nan_dataframe_time = DataFrame(np.random.randn(7, 3))
data_nan_dataframe_time.ix[:4, 1] = np.nan
data_nan_dataframe_time.ix[:2, 2] = np.nan
# print data_nan_dataframe_time
# print data_nan_dataframe_time.dropna(thresh=3)
# print data_nan_dataframe_time.dropna()


# 填充缺失数据

# 使用fillna来填充缺失值
# print data_nan_dataframe_time.fillna(0)
# 可以传递字典给fillna, 对于不同列填充不同的值
# print data_nan_dataframe_time.fillna({1: 0.5, 3: -1})
# fillna 默认是返回一个新的对象,不对原对象进行修改
# 设置inplace来选择是否对原对象进行修改
_ = data_nan_dataframe_time.fillna(0, inplace=True)
# print data_nan_dataframe_time

# 对于reindex有效的插值方法也可以用于fillna
df_reindex_fillna = DataFrame(np.random.randn(6, 3))
df_reindex_fillna.ix[2:, 1] = np.nan
df_reindex_fillna.ix[4:, 2] = np.nan
# print df_reindex_fillna
# print df_reindex_fillna.fillna(method='ffill')
# print df_reindex_fillna.fillna(method='ffill', limit=2)

# 用平均值填充
data_mean_fill = Series([1., np.nan, 3.5, np.nan, 7])
# print data_mean_fill.fillna(data_mean_fill.mean())
# print data_mean_fill.fillna(value=2)

# fillna函数的参数
# value 用于填充缺失值的标量值或者字典对象
# method 插值方式 如果函数调用时未指定其他参数的话。 默认为ffill
# axis 待填充的轴, 默认axis=0
# inplace 修改调用者对象,而不产生副本
# limit 对于前向填充或者后向填充, 可以连续填充的最大的数量