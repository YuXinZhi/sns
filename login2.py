# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

iedriver = "C:\Program Files\Internet Explorer\IEDriverServer.exe"
os.environ["webdriver.ie.driver"] = iedriver  #调用IE浏览器

browser = webdriver.Ie(iedriver)
browser.get('http://weibo.com/')  #需要打开的网址

user = browser.find_element_by_id("loginname") #审查元素username的id
user.send_keys("11111")  #输入账号
password = browser.find_element_by_name("password") #审查元素password的name
password.send_keys("1234")  #输入密码
password.send_keys(Keys.RETURN) #实现自动点击登陆
print('登陆成功')