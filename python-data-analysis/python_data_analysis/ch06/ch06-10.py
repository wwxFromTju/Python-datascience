#!/usr/bin/env python
# encoding=utf-8

import requests
import json

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 发送一个HTTP GET请求
# 旧的API,现在无法运行了
url = 'http://search.twitter.com/search.json?q=python%20pandas'
resp = requests.get(url)
print resp
# 很多Web API返回的是JSON字符串
data = json.loads(resp.text)
print data.keys()
tweet_fields = ['created_at', 'from_usrt', 'id', 'text']
tweets = DataFrame(data['results'], columns=tweet_fields)
print tweets
print tweets.ix[7]