#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 高级数组输入输出

# 内存映像文件
# 内存映像文件是一种将磁盘上的非常大的二进制数据文件当做内存中的数组进行处理
# Numpy实行了一个类似ndarray的memmap对象, 它允许将大文件分成小段读取, 而不是一次读取全部
# 基本上只要能用于ndarray的算法也就能用于memmap

# 使用np.memmap传入一个文件路径, 数据类型, 形状, 文件模式
mmap = np.memmap('mymmap', dtype='float64', mode='w+', shape=(10000, 10000))
print mmap

# 对memmap切片会返回磁盘上的数据视图
section = mmap[:5]
# 如果将数据赋值給视图, 那么数据会先被缓存在内存中(就是Python的文件对象), 然后调用flush来写入磁盘
section[:] = np.random.randn(5, 10000)
mmap.flush()
print mmap

# 如果某个内存映像超出了作用域, 那么会被垃圾回收器回收, 之前对其所做的任何修改都会被写入磁盘
# 打开一个已经存在的内存映像, 仍需要指明数据类型和形状, 因为磁盘上的那个文件只是块二进制数据, 没有元数据
mmap = np.memmap('mymmap', dtype='float64', shape=(10000, 10000))
print mmap

# 内存映像其实就是一个放在硬盘上的ndarra
