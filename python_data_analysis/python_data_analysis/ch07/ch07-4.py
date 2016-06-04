#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 合并重叠数据

a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b = Series(np.arange(len(a), dtype=np.float64),
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan
print a
print b
print pd.isnull(a)
# 在True的地方保留b的元素,在False替换为a中对应的元素
print np.where(pd.isnull(a), b, a)

# Series中有对应的combine_first
print b[:-2].combine_first(a[2:])

df1 = DataFrame({'a': [1., np.nan, 5., np.nan],
                 'b': [np.nan, 2, np.nan, 6.],
                 'c': range(2, 18, 4)})
df2 = DataFrame({'a': [5., 4. ,np.nan, 3., 7.],
                 'b': [np.nan, 3., 4., 6., 8.]})
print df1
print df2
print df1.combine_first(df2)