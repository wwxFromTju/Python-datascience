#!/usr/bin/env python
# encoding=utf-8

import numpy as np
import matplotlib.pyplot as plt

# 因为我单独开了个虚拟环境,在虚拟环境中无法调用外部

# 通常是使用ipython --pylab或者在ipython中输入%gui来进入gui事件循环
# 一条直线
# plot(np.arange(10))

# 新建一个Figure
fig = plt.figure()
# 创建一个2X2的图像
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

# 发出的绘图命令是默认在最后一个subplot上面绘图的
# 如果没有对应的subplot则会创建一个
# k--为黑色虚线
plt.plot(np.random.randn(50).cumsum(), 'k--')

# 可以指定对应的subplot上面画图
_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))

# 使用subplots创建新的Figure
# 可以通过axes来进行索引
fig, axes = plt.subplots(2, 3)

# 如果没有指定sharex sharey 则matplotlib可能会自动缩放各图标

# pyplot.subplots的选项
# nclos subplot的列数
# nrows subplot的行数
# sharex x轴刻度
# sharey y轴刻度
# subplot_kw 用于创建subplot的关键字字典
# **fig_kw 用于创建figure时的其他关键字

# 使用subplots_adjust函数来调整间距

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        # 使用axes来直接操作各个subplot
        axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0)

# 绿色虚线
x = range(10)
y = range(10)
ax1.plot(x, y, 'g--')
# 可以直接使用linestyle来指定线型, color指定颜色
ax2.plot(x, y, linestyle='--', color='g')
# 线型图可以加上一些标记marker
plt.plot(np.random.randn(30).cumsum(), 'ko--')
# 更为详细的形式
# plot(np.random.randn(30).cumsum(), color='k', linestyle='dashed', marker='o')

# 可以使用线性插值, 通过drawstyle选项
data = np.random.randn(30).cumsum()
plt.plot(data, 'k--', label='Default')
plt.plot(data, 'k--', drawstyle='steps-post', label='steps-post')
# 贴上标签
plt.legend(loc='best')
