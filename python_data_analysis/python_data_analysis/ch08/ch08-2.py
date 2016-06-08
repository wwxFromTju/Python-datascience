#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

# 由于我开的虚拟环境所以调用外部x11有点问题,所以建议下面代码在ipython的pylab模式下运行

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# 随机漫步
ax.plot(np.random.randn(1000).cumsum())

# 修改X轴刻度
# 使用 set_xticks / set_xticklabels
# set_xticks 设置数据范围
# set_xticklabels 设置对应的标签
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
# 第一个list为对应上面的刻度, rotation为旋转角度, fontsize为字大小
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],
                            rotation=30, fontsize='small')
# set_title 设置标题
ax.set_title('tju random go')
# set_xlable 为X轴设置标题
ax.set_xlabel('X label')
# set_ylable 为Y轴设置标题
ax.set_ylabel('Y label')


# 添加图例 legend
# 用于标识图表元素
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# 在添加subplot时使用lable
ax.plot(np.random.randn(1000).cumsum(), 'k', label='one')
ax.plot(np.random.randn(1000).cumsum(), 'k--', label='two')
ax.plot(np.random.randn(1000).cumsum(), 'k.', label='three')
# 然后使用ax.legend()或者plt.legend()来创建图例
# loc 为图例的位置
ax.legend(loc='best')
plt.legend(loc='right')


# 注解
# 通过 text/arrow/annotate等函数进行添加
# 前2个参数为(x,y),对应屏幕上的坐标
ax.text(5, 5, 'Hello world', family='monospace', fontsize=10)
