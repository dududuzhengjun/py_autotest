# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：add_student
@Author: duzhengjun
@create_time：2020/9/2 14:11
@detail：Don't stop learning!!!
@Motto：Sow nothing, reap nothing
"""
import _json
import requests

def login():
    """用户登录"""
    header1 = {
        "content-type": "application/json;charset=UTF-8"
    }

    data = {
        "loginName": "13002840927",
        "password": "JNqpgSlVSt5EjQoIdVPms4jYHm7OTvmlsBhk28NMYD5jJVSuLscI7WBqUeIzsbdd+4NsbviojTTdmuDrRi8G55AbR7hqilE6UNluqh9ep/c2tyuAIH67OR/jJpmVUWMijHzKyTenzoI9ydXEWMBsVQIY214mPvUk98bnSZTqaXs=",
    }
    login_url = "https://youxueketang.anoah.com/api/user/account/login"
    login_url_response = requests.post(login_url, headers=header1, json=data)
    """-*- coding:utf-8 –*-中文编码"""
    print("登录接口响应信息：", end="")
    print(login_url_response.json())

    # #将获取到的token返回
    return (login_url_response.json()["data"]["jwt"])
    print(jwt)

login()