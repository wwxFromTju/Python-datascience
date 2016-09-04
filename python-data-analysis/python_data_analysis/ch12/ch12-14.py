#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 使用结构化数组, 它可以将内存块解释为带有任意复杂嵌套的表格型结构, 所以数组中的每个元素在内存中
# 都被表示为固定的字节数, 所以可以提供非常快速高效的磁盘数据读写(包括内存映像),网络传输等

# 结构化数组的另一个常见用法是, 将数据文件写成定长记录字节流, 这是C和C++代码中常见的数据序列化手段
# 只要知道文件的格式(记录的大小, 元素的顺序, 字节数以及数据类型等) 就可以使用np.fromfile将数据读入内存

# 结构化数组操作:numpy.lib.recfunctions
# numpy.lib.recfunctions中有一些用于增删字段或执行基本连接运算的工具
# 一般都需要创建一个新数组来对dtype进行修改

# 和Python内置的列表一样, ndarray的sort也是就地排序, 就是在原数组上排序, 而不产生新数组
arr = np.random.randn(6)
print arr
# 就地排序
# 注意如果是视图view的话, 那么原数组会被修改
arr.sort()
print arr

# 视图上面排序
arr = np.random.randn(3, 5)
print arr
arr[:, 0].sort()
print arr

# numpy.sort会为原数组创建一个已排序副本。 接受参数和ndarray.sort一样
arr = np.random.randn(3, 5)
print arr
# 指定排序的轴, 每个部分单独排序
arr.sort(axis=1)
print arr

# 无法设置降序, 可以使用小技巧: 先排序, 然后[::-1]来获得降序
print arr[:, ::-1]

