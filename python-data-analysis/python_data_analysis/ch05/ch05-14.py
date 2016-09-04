#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 重排分级顺序
# 调整某条轴上各级别的顺序,或根据指定级别上的值对数据进行排序


frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', "Colorado"],
                           ['Green', 'Red', 'Green']])
# print frame
# 指定index或columns的names
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']

# swaplevel接受2个级别编号或者名称,并返回一个互换了级别的新对象(数据不变)
# print frame
# print frame.swaplevel('key1', 'key2')

#  sortlevel 根据单个级别中的值对数据进行排序(稳定排序)
# 1 == 'key2'
# print frame.sortlevel()
# print frame.sortlevel(1)

# 交换级别, 也会常用sortlevel来使得结果有序, 使得有序的索引被合并
# print frame.swaplevel(0, 1).sortlevel()

# 根据级别汇总统计
# 用level来指定统计的级别,默认为index
# print frame.sum(level='key2')
# 可以指定axis为1, 然后选择columns中的属性来进行统计
# print frame.sum(level='color', axis=1)
# 其实是利用pandas的groupby功能

# 使用DataFrame的列
frame_columns = DataFrame({'a': range(7), 'b': range(7, 0, -1),
                           'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                           'd': [0, 1, 2, 0, 1, 2, 3]})
# print frame_columns
# DataFrame的set_index函数会将其一个或者多个列转换为行索引, 并创建一个新的DataFrame
frame_columns_index = frame_columns.set_index(['c', 'd'])
# print frame_columns_index
# set_index 默认会将set的index从原来的地方移除
# 可以设置 drop来保留
# print frame_columns.set_index(['c', 'd'], drop=False)

# reset_index与set_index功能相反,将index转化到内部
# print frame_columns.reset_index()
