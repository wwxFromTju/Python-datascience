#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# pandas中的绘图函数

# 对于 DataFrame 和 Series 默认的绘图都是线性图
# Series 的索引为x轴,可以使用use_index=False来禁止该功能
# X/Y 轴的刻度和界限和通过xticks/yticks和xlim/ylim来进行调节
# 可选参数ax可以传入subplot来绘制对应为的图
s = Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot()
df = DataFrame(np.random.randn(10, 4).cumsum(0),
               columns=['A', 'B', 'C', 'D'],
               index=np.arange(0, 100, 10))
df.plot()

# Series.plot 的方法
# label 图例的标签
# ax为对应的ax对象, 默认为当前的subplot
# style 传给matplotlib的风格字符串
# alpha 图表的填充不透明度
# kind 可以为'line', 'bar', 'barh', 'kde'
# logy 在y轴使用对数标尺
# use_index 将对象的索引用作刻度标签
# rot 旋转刻度标签
# xticks 用作X轴刻度的值
# yticks 用作Y轴刻度的值
# xlim X轴的范围 [0, 10]之类的
# ylim Y轴的范围
# grid 显示网格线

s = Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot(label='series',alpha=0.1, kind='line', logy=True, rot=60, grid=True)