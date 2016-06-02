#!/usr/bin/env python
# encoding=utf-8

from lxml import objectify
from pandas import Series, DataFrame
from StringIO import StringIO

# XML Extensible Markup Language

path = 'Performance_MNR.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()
data = []
skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ', 'DESIRED_CHANGE', 'DECIMAL_PLACES']
for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)
perf = DataFrame(data)
print perf

tag = '<a href="http://www.google.com">Google</a>'
root = objectify.parse(StringIO(tag)).getroot()
print root
print root.get('href')
print root.text
