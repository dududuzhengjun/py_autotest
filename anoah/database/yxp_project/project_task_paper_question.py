# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：project_task_paper_question
@Author: duzhengjun
@create_time：2020/6/17 13:19
@detail：Don't stop learning!!!
@Motto：Sow nothing, reap nothing
"""
import random
import sys
import time
from datetime import datetime
import pymysql
from faker import Faker


conn = ""
cur = ""

records = []
count = 0

# 构造插入数据
def gen_data(count):
    global records
    f = Faker("zh_cn")
    for i in range(count):

        # `id` bigint(20) unsigned NOT NULL
        id = 1255380472670732290+i

        # `task_id` bigint(20) unsigned DEFAULT NULL COMMENT '任务ID'
        task_id = 1255380471735402499+i

        # `paper_id` bigint(20) unsigned DEFAULT NULL COMMENT '试卷ID'
        paper_id = 1234687096669679617+i

        # `question_id` bigint(20) unsigned DEFAULT NULL COMMENT '试题ID'
        question_id = 1134687095669689620+i

        # `is_valid` tinyint(2) unsigned DEFAULT '1' COMMENT '是否有效，1：有效，0：无效'
        is_valid_list = [0, 1]
        is_valid = random.choice(is_valid_list)

        # `created` datetime NOT NULL
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # `updated` datetime NOT NULL
        updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        r = (id, task_id, paper_id, question_id, is_valid, created, updated)
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
        db='yxp_project',
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
    sql = """INSERT INTO yxp_project.project_task_paper_question (  
                id,
                task_id, 
                paper_id, 
                question_id,
                is_valid,
                created,
                updated
            ) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    cursor.executemany(sql, records)
    conn.commit()
except:
    print("执行数据插入时发生错误")

finally:
    cursor.close()  # 关闭游标
    conn.close()  # 释放连接

end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print("开始时间: " + start_time)
print("完成时间：" + end_time)