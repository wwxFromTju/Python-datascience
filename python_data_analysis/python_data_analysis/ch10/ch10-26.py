#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 性能和内存使用方面的注意事项
# Timestamp/Period都是以64位整数表示的(Numpy的datetimes64数据类型)
# pandas会尽量在多个时间序列之间共享索引, 所以创建现有时间序列的视图不会占用更多内存
# 低频率索引会被放在一个中心缓存中, 所以任何固定频率的索引都是该日期缓存的视图

# 性能优化方面, pandas对数据对其(比如ts1 + ts2)和重采样运算进行了高度优化
# 下面将一亿个数据聚合成OHLC
rng = pd.date_range('1/1/2000', periods=100000000, freq='10ms')
ts = Series(np.random.randn(len(rng)), index=rng)
print ts

print ts.resample('15min', how='ohlc')

# 下面代码在ipython中运行
%timeit ts.resample('15min', how='ohlc')



# 运行时间和聚合结果的大小有关, 约高频率,时间越多
rng = pd.date_range('1/1/2000', periods=100000000, freq='1s')
ts = Series(np.random.randn(len(rng)), index=rng)
# 下面代码请在ipython中运行
%timeit ts.resample('15s', how='ohlc')

