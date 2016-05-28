#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 函数应用和映射

frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print frame
# 元素级绝对值
# print np.abs(frame)
# 可以使用DataFrame的apply方法,将函数运用来行或者列上,指定axis,默认是0,运用在列上
# print frame.apply(lambda x: x.max() - x.min())
# print frame.apply(lambda x: x.max() - x.min(), axis=1)

# 常见的数组统计方法已经实现了,所以对应常规的sum,mean这类的方法不需要apply来实现
def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])
# print frame.apply(f)

# 可以进行元素级的apply, 对应Series的map
# 将精度变化为2位小数
print frame.applymap(lambda x:'{:.2f}'.format(x))
