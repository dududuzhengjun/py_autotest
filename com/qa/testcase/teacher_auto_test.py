# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：teacher_auto_test
@Author: duzhengjun
@create_time：2020/8/15 19:37
@detail：Don't stop learning!!!
@Motto：Sow nothing, reap nothing
"""
# coding: utf-8

from appium import webdriver
import time
import os


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9.0'
desired_caps['deviceName'] = 'FAUKRWCA7S6S85V8DEF'
desired_caps['appPackage'] = 'com.anoah.uclass.pad.teacher'
desired_caps['appActivity'] = '.activity.LauncherActivity'
                # 'unicodeKeyboard': True,
                # 'resetKeyboard': True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
print("ceshi")
# os.system("adb shell am start -n com.anoah.uclass.pad.teacher")
driver.find_element_by_id("com.anoah.uclass.pad.teacher:id/iv_head").click()