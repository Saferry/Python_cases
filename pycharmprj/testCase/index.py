# !/usr/bin/env python
# -*-coding:utf-8-*-
# author:super

import time
from selenium import webdriver
# from package.module import *

driver=webdriver.Firefox() # 下载geckodriver放在python根目录下，地址：https://github.com/mozilla/geckodriver/releases
driver.get('http://www.baidu.com')
str1=u'百度一下，你就知道'
print driver.title
assert driver.title in str1
time.sleep(5)
driver.quit()