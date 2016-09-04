#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 二进制文件

# 使用Python内置的pickle序列化
# 但是很难保证该格式永远稳定,所以不建议使用

# 正常读取文本文件
frame = pd.read_csv('ex1.csv')
print frame
# 保存为2进制文件
frame.to_pickle('twofile')

# np.load()->pickle函数读取
print pd.read_pickle('twofile')

# 使用HDF5格式
# 是一个流行的工业库,是一个C库,带有语言接口
# HDF5-》HDF: hierarchical data format 层次型数据格式
# 含有一个文件系统式的节点结构,它使你能够存储多个数据集并支持元数据
# 支持多种压缩器的即时压缩,还能高效地存储重复模式数据
# 对于大的无法放入内存的数据集,可以使用HDF-》可以高效地分块读写

# 创建最小化类似于字典的HDFStore类,通过PyTables存储pandas对象
store = pd.HDFStore('mydata.h5')
frame = pd.read_csv('ex1.csv')
store['obj1'] = frame
store['obj1_col'] = frame['a']
print store
print store['obj1']
