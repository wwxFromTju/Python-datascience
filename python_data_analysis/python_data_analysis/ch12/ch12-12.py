#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 结构化和记录式数组
# ndarray是一种同质数据容器, 在它表示的内存块中, 各元素占用的字节数相同(具体根据dtype而定)
# 结构化数组是一种特殊的ndarray, 其中的各个元素可以被看做C语言的结构体(struct)或SQL表中带有多个命名字段的行
dtype = [('x', np.float64), ('y', np.int32)]
sarr = np.array([(1.5, 6), (np.pi, -2)], dtype=dtype)
print sarr

# 元组列表, 各元组的格式为(field_name, field_data_type)类似的
# 该对象的各个元素可以像字典那样进行访问
print sarr[0]
print sarr[0]['y']

# 字段名保存在dtype.names属性中。在访问结构化数组的莫个字段时, 返回的是该数据的视图, 所以不会发生数据复制
print sarr['x']



