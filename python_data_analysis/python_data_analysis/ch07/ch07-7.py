#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as pd
from pandas import Series, DataFrame

# 使用函数或映射进行数据转换
data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham',
                           'nova lox'],
                  'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print data

# 映射
meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'
}

# 通过映射来新增列
data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
print data

print data['food'].map(lambda x: meat_to_animal[x.lower()])

# map 是一个实现元素级别转换以及其他数据清理工作的快捷方法
