#!/usr/bin/env python
# encoding=utf-8

import re

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 矢量化字符串函数

data = {'Dave': 'dave@google.com',
        'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com',
        'Wes': np.nan}
data = Series(data)
print data

# 可以 map + 函数 运用字符串和正则表达式方法
# 但是下面的语句面对上面的nan会异常
# print data.map(lambda x: 'gmail' in x)

# Series使用了一些方法来跳过NA值检查
# 比如Series的str属性可以访问
# contains 判断是否含有对应的字符串
print data.str.contains('gmail')

# 使用正则表达式, 同时可以加上任意的re选项
pattern = '([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.([A-Z]{2,4})'
print pattern
print data.str.findall(pattern, flags=re.IGNORECASE)

# 实现矢量化元素获取
matches = data.str.match(pattern, flags=re.IGNORECASE)
print matches
print matches.str.get(1)
print matches.str[0]
# 对字符串进行子串截取
print data.str[:5]

# 矢量化的字符串方法

# cat 元素级的拼接,可以指定分隔符
print data.str.cat(sep='::')

# count 判断模式出现的次数
print data.str.count('gmail')

# endswith startswith 相当于每个元素来分别判断
print data.str.endswith('com')
print data.str.startswith('dave')

# join 采用指定的分隔符号将Series中字符串连接起来
print data.str.join(sep='-:-')

# len 计算字符串长度
print data.str.len()

# lower upper 转换大小写
print data.str.upper()
print data.str.lower()

# pad 在字符串的左右加上空白符号
print data.str.pad(10)
print data.str.pad(10, side='right')
print data.str.pad(10, side='both')

# center 相当指定pad的side=both
print data.str.center(19)

# repeat 重复字符串
print data.str.repeat(3)

# replace 替换字符串
print data.str.replace('dave', 'hehe')

# slice 根据分隔符或正则表达式对字符串进行拆封
print data.str.slice(start=0, stop=5, step=2)

# split 根据分隔符,正则表达式对字符串进行截取
print data.str.split(pattern)
print data.str.split('@')

# strip rstrip lstrip
# 类似Java去掉空白符