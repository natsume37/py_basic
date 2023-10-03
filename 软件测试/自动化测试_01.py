"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 自动化测试_01.py
@Author : 夏目&青一
@Time : 2022/11/9 12:33

"""
from selenium import webdriver

url = 'http://192.168.47.5:36331/suthr/mycenter'
used = 'stu211'
password = '123456'

web = webdriver.Chrome()
drive = web.get(url)
web.find_element_by_xpath('//*[@id="username"]').send_keys(' hrteacher')
web.find_element_by_id('password').send_keys('123456')
web.find_element_by_css_selector('button').click()