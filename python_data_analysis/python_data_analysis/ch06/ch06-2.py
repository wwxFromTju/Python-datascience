#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 逐块读取文件
# 在处理大文件时,或找出大文件中的参数集以便后续处理时,可以读取文件的一小部分或逐块对文件进行迭代

result = pd.read_csv('ex6.csv')
# 可以指定读取其中的几行,通过nrows来指定,即读取前几行
result_part = pd.read_csv('ex6.csv', nrows=5)
print result_part

# 可以读取逐块读取文件,需要设置chunksize(行数)
chunker = pd.read_csv('ex6.csv', chunksize=1000)
# chunker是一个TextFileReader
print chunker
tot = Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
# 降序,order修改为sort_values
tot = tot.sort_values(ascending=False)
print tot
print tot[:10]
# print chunker.get_chunk(500)
