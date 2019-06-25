# !/usr/bin/env python
# _*_ coding:utf-8 _*_

# author: super

# from module import *
# from package.module import *


# import sys
# print(sys.path)


# from selenium import webdriver
# print(help(webdriver.Firefox))
from selenium.webdriver.firefox.webdriver import WebDriver

driver = WebDriver.firefox_profile()  # type: WebDriver
# driver = webdriver.Firefox(executable_path='/Users/PC2016J9JKLM/geckodriver')
driver.get('http://www.baidu.com')
# str1='百度一下，你就知道'
print driver.title
print type(driver.title)
# assert driver.title in str1
driver.quit()
