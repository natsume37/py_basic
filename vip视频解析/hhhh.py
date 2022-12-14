"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : hhhh.py
@Author : 夏目&青一
@Time : 2022/10/14 18:23
https://mooc2-ans.chaoxing.com/mycourse/stu?courseid=221258875&clazzid=60766047&cpi=217041836&enc=ee7114c69643552a5cbdfa197462e571&t=1666074413360&pageHeader=0&v=2

"""
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
borw = webdriver.Chrome()

borw.get('https://mooc2-ans.chaoxing.com/mycourse/stu?courseid=221258875&clazzid=60766047&cpi=217042052&enc=3d54eef1fa610c138de95ed7432089b4&t=1666084656653&pageHeader=1&v=2')
# a = borw.find_element_by_xpath('//*[@id="post-34"]/div/p[3]/a').get_attribute("href")

# print(a)
# 登录到章节学习
borw.find_element_by_xpath('//*[@id="phone"]').send_keys('16608855782')
borw.find_element_by_xpath('//*[@id="pwd"]').send_keys('Dsq20020926')
borw.find_element_by_xpath('//*[@id="loginBtn"]').click()

# 进入学习
frame_content = borw.find_element_by_xpath('//*[@id="frame_content-zj"]')  #进入fram
borw.switch_to.frame(frame_content)

time.sleep(1)

all_not_wach = borw.find_elements_by_xpath('')