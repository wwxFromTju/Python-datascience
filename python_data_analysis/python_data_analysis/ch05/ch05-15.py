#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import pandas.io.data as web


# 整数索引
ser = Series(np.arange(3.))
# 注意和一般的Python索引不一样,对于是数字索引-1会产生异常
# -1对于数字索引不好解释
# print '-1导致异常', ser[-1]
# 默认索引是从0开始的整数,所以很难解释索引的意义
print '一般的索引从0开始', ser
# 比方我在索引中明确指定有-1的索引,那么-1是指我的索引还是最后一个呢?所以禁止-1在不包含-1的数字索引中使用
ser_neg = Series(np.arange(3.), index=[-1, 2, 3])
print '含有-1的索引直接访问的就是-1索引的值', ser_neg[-1]

# 可以指定为字符型索引,使得索引的解释性提升
ser2 = Series(np.arange(3.), index=['a', 'b', 'c'])
# 对于字符型索引-1不会有二义性
print '字母索引可以直接使用-1来访问最后一个', ser2[-1]

# 如果轴索引含有索引器, 那么根据整数进行数据选取操作,是面向标签的,不是面向排序的
print '3是面向标签的,不是面向位置的', ser_neg.ix[:3]

# 可靠的,不考虑索引类型和基于位置的索引
# 使用Series的iget_value
ser3 = Series(range(3), index=[-5, 1, 3])
# 这个future可能会被取消,尽量使用等价的那个
print ser3.iget_value(2)
# 等价于
print ser3.iloc[2]
# 对于frame可以使用irow
frame = DataFrame(np.arange(6).reshape(3, 2), index=[2, 0, 1])
# 下面这个future可能会被取消,所以尽量使用等价的那一个
print frame.irow(0)
print frame.iloc(0)

# 面板数据
# pandas有一个Panel数据结构, 可以理解为一个三维版本的DataFrame
pdata = pd.Panel(dict((stk, web.get_data_yahoo(stk, '1/1/2009', '6/1/2012')) for stk in ['AAPL', 'GOOG', 'MSFT', 'DELL']))
print 'Panel', pdata
# Panel的每一项都是DataFrame
# 交换2个轴
pdata = pdata.swapaxes('items', 'minor')
print pdata['Adj Close']
# 基于ix的标签索引被推广到三个维度
print pdata.ix[:, '6/1/2012', :]
print pdata.ix['Adj Close', '5/22/2012':, :]

# 呈现面板数据,尤其是面对拟合统计模型,使用"堆积式的"DataFrame形式
stacked = pdata.ix[:, '5/30/2012':, :].to_frame()
print stacked
# to_panel是to_frame的逆运算
print stacked.to_panel