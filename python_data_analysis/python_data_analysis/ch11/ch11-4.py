#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 拼接多个数据源
# 在一个特定的时间点上, 从一个数据源切换到另一个数据源
# 用另一个时间序列对当前时间序列中的缺失值'打补丁'
# 将数据中的符号(国家, 资产代码等)替换为实际数据

data1 = DataFrame(np.ones((6, 3), dtype=float),
                  columns=['a', 'b', 'c'],
                  index=pd.date_range('6/12/2012', periods=6))
print data1

data2 = DataFrame(np.ones((6, 3), dtype=float) * 2,
                  columns=['a', 'b', 'c'],
                  index=pd.date_range('6/13/2012', periods=6))
print data2

# 将2个数据合并
spliced = pd.concat([data1.ix[:'2012-06-14'], data2.ix['2012-06-15':]])
print spliced

# 多了d列
data2 = DataFrame(np.ones((6, 4), dtype=float) * 2,
                  columns=['a', 'b', 'c', 'd'],
                  index=pd.date_range('6/13/2012', periods=6))

# 将2个数据再一次拼接, 对于data1上面没有的D则补全NaN
spliced = pd.concat([data1.ix[:'2012-06-14'], data2.ix['2012-06-15':]])
print spliced

# 将合并之前的数据来填充NaN值
spliced_filled = spliced.combine_first(data2)
print spliced_filled

# 就地更新
spliced.update(data2, overwrite=False)
print spliced

# 替换对应的列
cp_spliced = spliced.copy()
cp_spliced[['a', 'c']] = data1[['a', 'c']]
print cp_spliced
