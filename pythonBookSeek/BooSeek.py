#!/usr/bin/env python

from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import time

url = "http://202.113.6.238/opac/book/578253?globalSearchWay="

driver = webdriver.Firefox()
driver.get("http://202.113.6.238/opac/book/578253?globalSearchWay=")
time.sleep(0.1)

print(driver.page_source)


html = urlopen("http://202.113.6.238/opac/book/578253?globalSearchWay=")
page = BeautifulSoup(html)
iframexx = page.find_all("",{"iframe":"duxiuframe"})
print(iframexx)
print(iframexx.attrs["src"])
print(page)
#print(page("iframe"))

