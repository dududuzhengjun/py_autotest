# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：publish_user
@Author: duzhengjun
@create_time：2020/6/20 11:21
@detail：Don't stop learning!!!
@Motto：Sow nothing, reap nothing
"""
import random
import sys
import time
from datetime import datetime
import pymysql
from faker import Faker
import uuid

conn = ""
cur = ""

records = []
count = 0


# 构造插入数据
def gen_data(count):
    global records
    f = Faker("zh_cn")
    for i in range(count):
        # `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '编号id',
        id = 37865 + i

        #   `publish_id` char(22) NOT NULL COMMENT '发布ID',
        publish_id = str(
            f.password(
                length=22,
                special_chars=False,
                digits=True,
                upper_case=True,
                lower_case=True,
            )
        )

        # `user_id` char(22) NOT NULL COMMENT '用户id',
        user_id = int(f.random.randint(1, 10000))

        # `class_id` char(22) NOT NULL COMMENT '班级id',
        class_id_list = [1265119369965383682, 1265119369965383683]
        class_id = random.choice(class_id_list)

        # `role` tinyint(4) NOT NULL DEFAULT '0' COMMENT '角色 1-是(游客) 0-否（本班学生） 7-24苏利军添加',
        role_list = [0, 1]
        role = random.choice(role_list)


        # `join_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '参与状态 1(上过课) 0(未上课)  7-24苏利军添加',
        join_status_list = [0, 1]
        join_status = random.choice(join_status_list)

        # `revise_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '作业的订正状态 \r\n0 无需订正(没有试题错误 即作业正确率为100, 或作业资源均为学习类) \r\n1 已订正(所有试题已提交订正 并且所有客观题订正后的正确率为100)\r\n2 未订正(有客观题订正后的正确率不为100 或有主观题 未提交订正)',
        revise_status_list = [0, 1, 2]
        revise_status = random.choice(revise_status_list)

        #   `created` datetime NOT NULL COMMENT '创建时间',
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #   `updated` datetime NOT NULL COMMENT '更新时间',
        updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        r = (id,
             publish_id,
             user_id,
             class_id,
             role,
             join_status,
             revise_status,
             created,
             updated)
        records.append(r)


start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
gen_data(count)

try:
    # 创建一个数据库连接
    conn = pymysql.connect(
        host='192.168.46.36',
        port=3306,
        user='dzj',
        passwd='dzj',
        db='yxp_publish',
        charset='utf8'
        # host='localhost',
        # port=3306,
        # user='root',
        # passwd='940927',
        # db='test',
        # charset='utf8'
    )

    # 创建一个游标对象
    cursor = conn.cursor()
except Exception:
    print("数据库连接失败")
    sys.exit()

sql = ""
try:
    # 批量执行SQL语句
    sql = """INSERT INTO yxp_publish.publish_user (  
                id,
                publish_id,
                user_id, 
                class_id,
                role,
                join_status,
                revise_status,
                created,
                updated
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.executemany(sql, records)
    conn.commit()
except pymysql.Error as e:
    print("执行数据插入时发生错误")
    print(e.args[0], e.args[1])

finally:
    cursor.close()  # 关闭游标
    conn.close()  # 释放连接

end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print("开始时间: " + start_time)
print("完成时间：" + end_time)
