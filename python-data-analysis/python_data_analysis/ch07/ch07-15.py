#!/usr/bin/env python
# encoding=utf-8

import re

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 正则表达式
# 正则表达式通常被称为regex, 提供的是一种灵活的文本搜索或匹配字符串模式的方式

text = 'foo bar\t baz  \tqux'
print text
# \s+ 一个或多个空白符
print re.split('\s+', text)

# 可以通过re.compile来自己编译regex来获得可重用的regex对象
regex = re.compile('\s+')
print regex.split(text)

# 得到匹配的所有模式
print regex.findall(text)

# 如果一个模式实用的多,那么compile是一个比较好的选择
text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@gmail.com
"""

pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'

regex = re.compile(pattern, flags=re.IGNORECASE)

# 返回一组电子邮件
print regex.findall(text)
# 返回第一个电子邮件
# 以位置返回
m = regex.search(text)
print m
print text[m.start():m.end()]
# 返回None,只匹配出现在字符串开头的模式
print regex.match(text)

# sub将匹配到模式替换为指定的字符串
print regex.sub('REDACTED', text)

pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern, flags=re.IGNORECASE)

m = regex.match('wesm@bright.net')
print m.groups()

print regex.findall(text)

print regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text)

regex = re.compile(r"""
(?P<username>[A-Z0-9._%+-]+)
@
(?P<domain>[A-Z0-9.-]+)
\.
(?P<suffix>[A-Z]{2,4})""", flags=re.IGNORECASE|re.VERBOSE)
m = regex.match('wesm@bright.net')
print m.groupdict()

# findall finditer  返回所有非重叠匹配模式, 一个是list 一个是迭代器
# match 从字符串开头位置匹配,只匹配开头位置,没有为None
# search 扫描全部字符串来匹配,如果有则匹配第一个
# split 拆分
# sub subn 替换