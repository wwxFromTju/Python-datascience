#!/usr/bin/env python
# encoding=utf-8

import sys

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 将数据输出到文本格式

data = pd.read_csv('ex5.csv')
print data
# 利用DataFrame的to_csv方法,可以将数据写到一个以逗号分隔的文件中
data.to_csv('csv2out.csv')

# 可以用sep指定分隔符
data.to_csv(sys.stdout, sep='|')

# 缺失值默认输出为空,可以用na_rep来指定输出什么
data.to_csv(sys.stdout,na_rep='NULL')

# 默认输出行和列的索引,即index与colunms
# 用index,header来控制是否输出
data.to_csv(sys.stdout, index=False, header=False)

# 可以只输出一部分的列,并且可以指定排序顺序
# 注意更新为col-》colunms
data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])

# Series也有对应的to_csv
dates = pd.date_range('1/1/2000', periods=7)
ts = Series(np.arange(7), index=dates)
ts.to_csv('series2out.csv')

# Series读取csv文件
ser_csv = Series.from_csv('series2out.csv', parse_dates=True)
print ser_csv
