#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 读取Excel文件
xls_file = pd.ExcelFile('test_multisheet.xls')
print xls_file.sheet_names
print xls_file.parse('Alpha')