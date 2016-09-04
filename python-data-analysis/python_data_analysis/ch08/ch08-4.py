#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
from pandas import Series, DataFrame

# 常见图形
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color='r', alpha=0.3)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]], color='g', alpha=0.5)

ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)


# 保存图标
plt.savefig('figpath.svg')
# 指定对应的dip和设置bbox_inches:可以去掉图标周围的白边
plt.savefig('figpath2.svg', dip=400, bbox_inches='tight')

# 可以将文件保存到任意的文件型对象
# buffertemp = StringIO()
# plt.savefig(buffertemp)
# plot_data = buffertemp.getvalue()

# Figure.savefig() 选项
# fname 路径名的字符串或者Python的文件型对象。图像格式由扩张名推断
# dpi (每英寸点数)图像分辨率, 默认100
# facecolor/edgecolor 图像的背景色, 默认为w白色
# bbox_inches 图表需要保存的部分。如果设置为tight,则剪除图表周围的空白部分


# matplotlib 配置
# 可以自定义图像大小/subplot边距/配色方案/字体大小/网格类型等等
# 修改默认全局的图像默认大小设置为10x10, 第一个参数为希望自定义的对象
plt.rc('figure', figsize=(10, 10))
# 可以带上一些列的关键字
font_options = {'family': 'monospace',
                'weight': 'bold',
                'size': 10}
plt.rc('font', **font_options)

# 也可以配置matplotlibrc,当使用matplotlib会加载该文件