#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/28 17:06
from selenium import webdriver
browser = webdriver.Firefox()
print(type(browser))
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('card-img-top img-fluid')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
# linkElem = browser.find_element_by_link_text('Read It Online')
# linkElem.click()
