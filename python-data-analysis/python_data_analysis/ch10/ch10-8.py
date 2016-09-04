#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pytz
from pandas import Series, DataFrame


# 时区处理

# 夏令时(DST) / 协调世界时(UTC 格林尼治标准时间 Greenwich Mean Time)
# 时间是以UTC偏移量的形式准备的。
# 在python中通常使用pytz库, pytz库可以使用Olson数据库(汇编了世界时区信息)

# 察看对应的时区, 可以在对应的文档中看到
print pytz.common_timezones[-5:]

# 获得对应的时区对象
tz = pytz.timezone('US/Eastern')
print tz

# pandas中方法既可以接受时区名, 也可以接受时区对象, 建议只用时区名

# 本地化和转化
# pandas中时间序列默认是 单纯的(naive)时区
rng = pd.date_range('3/9/2012 9:30', periods=6, freq='D')
ts = Series(np.random.randn(len(rng)), index=rng)

# tz字段索引为None
print ts.index.tz

# 在生成日期范围的时候可以加上一个时区集
print pd.date_range('3/9/2012 9:30', periods=10, freq='D', tz='UTC')

# 从单纯(naive)到本地化的转换是通过tz_localize方法
ts_utc = ts.tz_localize('UTC')
print ts_utc
print ts_utc.index

# 被本地化后, 可以通过tz_convert转换到别的时区
print ts_utc.tz_convert('US/Eastern')

# 对于跨越夏令时转变期, 我们可以先本地化到EST,然后在转换到UTC或者柏林时间
ts_eastern = ts.tz_localize('US/Eastern')
print ts_eastern.tz_convert('UTC')
print ts_eastern.tz_convert('Europe/Berlin')

# 下面的也是DatetimeIndex的实例方法
print ts.index.tz_localize('Asia/Shanghai')



