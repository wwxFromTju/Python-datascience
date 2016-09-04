#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# Series,DataFrame所用到的任何数组和其他序列的标签都会被转换为一个index(pandas索引对象)
obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index
# print index
# print index[1:]

# index对象是不可修改的(immutable)
# 下面的代码会报一个错误:
# TypeError: Index does not support mutable operations
# index[1] = 'd'

# 因为不可以修改,可以使得index对象在多个数据结构之间安全共享
index = pd.Index(np.arange(3))
obj2 = Series([1.5, -2.5, 0], index=index)
# print obj2.index is index

# Index可以被继承从而实现特别的轴索引功能

# index的功能类似一个固定大小的集合
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame_in_dict = DataFrame(pop)
# print 'Ohio' in frame_in_dict.columns
# print 'Tju' in frame_in_dict.columns
# print 2001 in frame_in_dict.index
# print 2003 in frame_in_dict.index

# index的方法和属性
# append 连接另一个index对象,产生一个新的index
# diff 差集,得到一个index
# intersection 交集
# union 并集
# isin 判断指示各值是否都包含在参数集合中的布尔型数组
# delete 删除索引i处的元素,并得到新的index
# drop 删除传入的值,并得到新的index
# insert 将元素插入到索引i处,并得新的index
# is_monotonic 当元素升序(包括 等 ), 那么返回true
# is_unique 当index没有重复值的时候,返回true
# unique index中唯一值的数组
