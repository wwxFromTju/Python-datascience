#!/usr/bin/env python
# encoding=utf-8

import json

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# JSON(JavaScript Object Notation)

obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},
                {"name": "Katie", "age": 33, "pet": "Cisco"}]
}
"""

#  读取JSON字符串并转换为Python形式
result = json.loads(obj)
print result

# 将Python对象转换为JSON格式
asjson = json.dumps(result)
print asjson

# 将JSON对象转换为DataFrame
# 向Python构造器传入一组JSON对象,并选取数据字段的子集
siblings = DataFrame(result['siblings'], columns=['name', 'age'])
print siblings
