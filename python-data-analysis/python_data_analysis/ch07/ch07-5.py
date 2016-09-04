#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 重塑和轴向索引
# 重新排列表格型数据的基础运算。也称为重塑reshape或轴向旋转pivot

# 重塑层次化索引
# stack 将数据的列旋转为行
# unstack 将数据的行旋转为列
data = DataFrame(np.arange(6).reshape((2, 3)),
                 index=pd.Index(['Ohio', 'Colorado'], name='state'),
                 columns=pd.Index(['one', 'two', 'three'], name='number'))
print data

# 使用stack方法,将列旋转为行,得到一个Series
result = data.stack()
print result

# 对于一个层次化的Series,可以使用unstack来重排为一个DataFrame
# 默认情况是最内层
print result.unstack()
# 可以通过传入参数分层级别的编号或者名称来对别的级别的unstack操作
print result.unstack(0)
print result.unstack('state')

# 如果不是所有级别值都能在各分组中找到的话,那么unstack会引入缺失值
s1 = Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = Series([4, 5, 6], index=['c', 'd', 'e'])
data2 = pd.concat([s1, s2], keys=['one', 'two'])
print data2
print data2.unstack()

# stack会滤除缺失数据,所以该运算是可逆的
print data2.unstack().stack()
print data2.unstack().stack(dropna=False)

# 对DataFrame进行unstack进行操作时, 被旋转的会变成最内层
df = DataFrame({'left': result, 'right': result + 5},
               columns=pd.Index(['left', 'right'], name='side'))
print df.unstack('state')
print df.unstack('state').stack('side')

