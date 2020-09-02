# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：addressbook_adduser
@Author: duzhengjun
@create_time：2020/5/17 10:37
@detail：Don't stop learning!!!
@Motto：Sow nothing, reap nothing
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()



#用户登录
def user_login():
    driver.get("https://www.youxueketang.com/")
    print("已经成功打开浏览器并进入优学课堂首页")
    driver.maximize_window()
    driver.find_element_by_xpath("//*[@id='pane-0']/form/div[1]/div/div/input").click()

    # 获取打开的多个窗口句柄
    windows = driver.window_handles
    # 切换到当前最新打开的窗口
    driver.switch_to.window(windows[-1])




