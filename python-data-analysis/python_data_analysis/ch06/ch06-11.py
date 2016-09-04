#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import pandas.io.sql as sql

# 使用数据库
import sqlite3

query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
c REAL,         d INTEGER
);
"""

con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()

data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"

con.executemany(stmt, data)
con.commit()

curosr = con.execute('select * from test')
rows = curosr.fetchall()
print rows
print curosr.description
print DataFrame(rows, columns=zip(*curosr.description)[0])

print sql.read_sql('select * from test', con)