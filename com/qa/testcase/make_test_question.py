# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：make_test_question
@Author: duzhengjun
@create_time：2020/6/15 14:31
@detail：Don't stop learning!!!
@Motto：Sow nothing, reap nothing
"""
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

driver.get("https://www.youxueketang.com/")
print("已经成功打开浏览器并进入优学课堂首页")

# 用户登录
try:
    driver.maximize_window()
    driver.find_element_by_xpath("//*[@id=\"yxp_website\"]/header/div/div/div[2]").click()  # 点击右上角登录button进入登录页
    # 切换到最后一个窗口的句柄
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])
    driver.find_element_by_xpath("//*[@id=\"pane-0\"]/form/div[1]/div/div/input").send_keys("13002840927")  # 输入用户名
    driver.find_element_by_xpath("//*[@id=\"pane-0\"]/form/div[2]/div/div/input").send_keys("dzj111")  # 输入密码
    driver.find_element_by_xpath("//*[@id=\"pane-0\"]/form/div[3]/div/button").click()  # 点击登录按钮
    print("用户已成功登录")
    sleep(2)
except Exception:
    print("服务器正在构建，请稍后再试")

# 切换单位
driver.find_element_by_xpath("//*[@id=\"yxpProtal\"]/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/p").click()     # 点击用户头像打开个人中心
sleep(2)
driver.find_element_by_xpath(".//div[@class=\"nav-ident-tag\"]").click()    # 点击切换
sleep(2)
driver.find_element_by_xpath("//div[@class=\"el-select-dropdown el-popper ident-popper\"]/div[1]/div[1]/ul/li[1]/span").click() # 选择荷叶一小
sleep(2)
print("用户单位已切换至荷叶一小")


# 创建一道单选题
driver.find_element_by_xpath("//*[@id=\"yxpProtal\"]/div/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div/ul/li[3]").click() #点击进入我的资源




