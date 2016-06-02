#!/usr/bin/env python
# encoding=utf-8

import requests

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

url = 'http://search.twitter.com/search.json?q=python%20pandas'
resp = requests.get(url)
print resp
