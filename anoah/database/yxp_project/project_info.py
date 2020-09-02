# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：project_info
@Author: duzhengjun
@create_time：2020/6/17 18:09
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

        # `project_id` bigint(20) unsigned NOT NULL,
        project_id = 1251093992435630083+i

        #   `project_type` varchar(50) DEFAULT NULL COMMENT 'base_data_dictionary.type=PRJECT_TYPE',
        project_type_list = [1, 2]
        project_type = random.choice(project_type_list)

        #   `period_id` int(11) DEFAULT NULL COMMENT '学段',
        period_id_list = [3, 2]
        period_id = random.choice(period_id_list)

        #   `subject_id` int(11) DEFAULT NULL COMMENT '学科',
        subject_id = int(f.random.randint(1, 10))

        #   `project_scope` varchar(50) DEFAULT NULL COMMENT '项目范围,由所选的资源名称自动生成',
        project_scope = str(f.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))

        #   `name` varchar(50) DEFAULT NULL COMMENT '项目名称',
        name = str(f.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))

        #   `user_id` int(11) unsigned DEFAULT NULL COMMENT '创建人',
        user_id = int(f.random.randint(1, 1000000))

        #   `org_id` bigint(20) unsigned DEFAULT NULL COMMENT '发布单位',
        org_id = 1

        #   `source_address` varchar(500) DEFAULT NULL COMMENT '资料地址',
        source_address = str(f.address())

        #   `status` tinyint(2) DEFAULT NULL COMMENT '项目状态，1-进行中，2-已结束',
        status_list = [1, 2]
        status = random.choice(status_list)

        #   `source_type` varchar(50) NOT NULL COMMENT '知识库类型base_data_dictionary.type=SOURCE_TYPE',
        source_type_list = [1, 2, 3]
        source_type = random.choice(source_type_list)

        #   `source_id` bigint(20) NOT NULL COMMENT '知识库表ID',
        source_id = int(f.random.randint(1, 100))

        #   `is_deleted` tinyint(2) unsigned DEFAULT NULL,
        is_deleted_list = [0, 1]
        is_deleted = random.choice(is_deleted_list)

        #   `created` datetime DEFAULT NULL,
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #   `updated` datetime DEFAULT NULL,
        updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


        # `remark` varchar(255) DEFAULT NULL COMMENT '备注'
        remark = str(f.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)+"的备注")

        r = (project_id, project_type, period_id, subject_id, project_scope, name, user_id, org_id, source_address,
             status, source_type, source_id, is_deleted, created, updated)
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
    sql = """INSERT INTO yxp_project.project_info (  
                project_id,
                project_type, 
                period_id, 
                subject_id,
                project_scope,
                name,
                user_id,
                org_id,
                source_address,
                status,
                source_type,
                source_id,
                is_deleted,
                created,
                updated
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
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