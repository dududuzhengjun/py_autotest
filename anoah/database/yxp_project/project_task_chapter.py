# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：project_task_chapter
@Author: duzhengjun
@create_time：2020/6/17 10:39
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
        id = 1251094148971249667+i

        # `task_id` bigint(20) unsigned DEFAULT NULL
        task_id = 1251094148799283202+i

        # `chapter_id` int(11) unsigned DEFAULT NULL COMMENT '章节ID'
        chapter_id = int(f.random.randint(0, 10000))

        # `chapter_name` varchar(255) DEFAULT NULL COMMENT '章节目录名字'
        chapter_name = str(f.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))

        # `created` datetime NOT NULL
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # `updated` datetime NOT NULL
        updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        r = (id, task_id, chapter_id, chapter_name, created, updated)
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
    sql = """INSERT INTO yxp_project.project_task_chapter (  
                id,
                task_id, 
                chapter_id, 
                chapter_name,
                created,
                updated
            ) VALUES (%s,%s,%s,%s,%s,%s)"""
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