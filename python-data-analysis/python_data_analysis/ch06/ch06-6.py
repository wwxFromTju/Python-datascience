#!/usr/bin/env python
# encoding=utf-8
from urllib2 import urlopen
from lxml.html import parse
import pandas as pd
import numpy as np
from pandas.io.parsers import TextParser
from pandas import Series, DataFrame

# XML和HTML

# 通过指定kind来获得列名或数据
def _unpack(row, kind='td'):
    elts = row.findall('.//%s' % kind)
    return [val.text_content() for val in elts]

# 从一个table获得列名和数据
def parse_options_data(table):
    rows = table.findall('.//tr')
    header = _unpack(rows[0], kind='th')
    data = [_unpack(r) for r in rows[1:]]
    return TextParser(data, names=header).get_chunk()

# 使用urlopen打开网页,然后使用lxml解析得到数据流
parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=APPL+Options'))
print parsed
doc = parsed.getroot()
print doc

# 使用XPath来访问各个标签
# 访问所有的URL链接
links = doc.findall('.//a')
# 为HTML元素的对象,要得到URL和链接文本,必须使用各对象的get(URL)和text_content(针对显示的文本)
print links[15:20]
lnk = links[28]
print lnk
print lnk.get('href')
print lnk.text_content()

# 使用list comprehension列表推导式来获得所有的URL
urls = [lnk.get('href') for lnk in doc.findall('.//a')]
print urls[-10:]


# tables = doc.findall('.//table')
# calls = tables[0]
# puts = tables[1]

# rows = calls.findall('.//tr')
# 标题行
# print _unpack(rows[0], kind='th')
# 数据
# print _unpack(rows[1], kind='td')

# call_data = parse_options_data(calls)
# put_data = parse_options_data(puts)
# print call_data[:10]




