#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 透视表(pivot table)和交叉表(crosstab)
# 透视表就是通过设置行列的索引来构建对应的矩形区域来放置对应的数据


tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']

# 透视表

# 注意key的变化rows -> index, cols -> columns
# 在行上形成层次结构
print tips.pivot_table(index=['sex', 'smoker'])
# index为对应的行, colunms为对应的列, 然后再将tip_pct/size分开
print tips.pivot_table(['tip_pct', 'size'], index=['sex', 'day'], columns='smoker')
# 可以设置margins来统计列上的total
print tips.pivot_table(['tip_pct', 'size'], index=['sex', 'day'], columns='smoker', margins=True)
# 可以使用聚合函数, 通过传给aggfunc
print tips.pivot_table('tip_pct', index=['sex', 'smoker'], columns='day', aggfunc=len, margins=True)
# 填充缺失值
print tips.pivot_table('size', index=['time', 'sex', 'smoker'], columns='day', aggfunc='sum', fill_value=0)

# values 待聚合的列的名称
# index 用于分组的列名或其他分组键, 出现在透视表的行
# columns 用于分组的列名或其他分组键, 出现在透视表的列
# aggfunc 聚合函数或函数列表, 默认为'mean', 可以是任何对groupby有效的函数
# fill_value 用于替换缺失值
# margins 添加行/列小计和总计, 默认为False


# 交叉表 cross-tabulation

# 第一个参数为行, 第二个参数为列
print pd.crosstab([tips.time, tips.day], tips.smoker, margins=True)

