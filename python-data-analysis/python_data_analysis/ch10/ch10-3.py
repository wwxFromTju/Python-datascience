#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from datetime import datetime

# 时间序列基础

# 最基本的时间序列: 以时间戳为索引的Series
dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7),
         datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]

# 这些datetime对象实际上是被放在一个DatetimeIndex中
# ts视为TimeSeries
# 在现在这个pandas中, 将TimeSeries忽略掉了, 请使用Series, 不要显示使用TimeSeries
ts = Series(np.random.randn(6), index=dates)
print ts
print type(ts)
print ts.index

# 不同索引的时间序列之间的算术运算会自动按照日期对齐
# 没有相应索引的填充NaN
print ts + ts[::2]

# 类型使用Numpy的datetime64数据类型以纳米形式存储时间戳
print ts.index.dtype

# DatetimeIndex中各个标量值是pandas的Timestamp对象
stamp = ts.index[0]
print stamp


# 索引, 选取, 子集构造
# TimeSeries是Series的子类(现在被处理在Series了), 所以在索引和数据选取方面行为一样
stamp = ts.index[2]
print ts[stamp]

# 直接传入可以解释为日期的字符串
print ts['1/10/2011']
print ts['20110110']

# 对于较长的时间序列, 只传入年或年月即可
longer_ts = Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
print longer_ts
# 选出2001年
print longer_ts['2001']

# 通过日期进行切片, 只对规则Series有效
print ts[datetime(2011, 1, 7):]

# 大部分时间序列是按照时间先后排序的, 所以也可以用不存在的时间戳来指定切片的范围
print ts['1/6/2011': '1/11/2011']
# 等价于
print ts.truncate(after='1/11/2011', before='1/6/2011')

# 同样操作可以作用于DataFrame
dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
long_df = DataFrame(np.random.randn(100, 4),
                    index=dates,
                    columns=['Colorado', 'Texas', 'New York', 'Ohio'])
print long_df.ix['5-2001']