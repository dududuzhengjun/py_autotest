# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：paper_audit_question_attribute
@Author: duzhengjun
@create_time：2020/6/17 19:25
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
count = 999549


# 构造插入数据
def gen_data(count):
    global records
    f = Faker("zh_cn")
    for i in range(count):
        # `id` bigint(20) unsigned NOT NULL,
        id = 1250264344671920131+i

        #   `paper_audit_question_id` bigint(20) DEFAULT NULL COMMENT '表 paper_audit_question ID',
        paper_audit_question_id = 1250262090736836610+i

        #   `attribute_code` varchar(255) DEFAULT NULL COMMENT '试题属性',
        attribute_code_list = ["prompt", "body", "answer", "comment", "tip", "explanation"]
        attribute_code = random.choice(attribute_code_list)

        #   `check_content` text COMMENT '检查的内容',
        check_content = str(f.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))

        #   `updated_content` text COMMENT '修改的内容',
        updated_content = str(f.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))

        #   `is_report_error` tinyint(2) DEFAULT '0' COMMENT '是否报错 1.报错 0.未报错  默认0',
        is_report_error_list = [0, 1]
        is_report_error = random.choice(is_report_error_list)

        #   `is_checked` tinyint(2) DEFAULT '0' COMMENT '是否检查出埋错,1:检查出，0:未检查出',
        is_checked_list = [0, 1]
        is_checked = random.choice(is_checked_list)

        #   `is_knowledge_error` tinyint(2) DEFAULT '0' COMMENT '是否是知识性错误,1:是，0:不是',
        is_knowledge_error_list = [0, 1]
        is_knowledge_error = random.choice(is_knowledge_error_list)

        #   `child_question_number` smallint(4) DEFAULT NULL COMMENT '子题目编号',
        child_question_number_list = [0, 1, 2, 3, 4]
        child_question_number = random.choice(child_question_number_list)

        #   `main_question` tinyint(2) DEFAULT NULL COMMENT '是否为主题目, 1.主题目，0.非主题目',
        main_question_list = [0, 1]
        main_question = random.choice(main_question_list)

        #   `created` datetime NOT NULL,
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #   `updated` datetime NOT NULL,
        updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #   `is_lurked` tinyint(2) DEFAULT '0' COMMENT '是否埋错',
        is_lurked_list = [0, 1]
        is_lurked = random.choice(is_lurked_list)



        r = (id,
             paper_audit_question_id,
             attribute_code,
             check_content,
             updated_content,
             is_report_error,
             is_checked,
             is_knowledge_error,
             child_question_number,
             main_question,
             created,
             updated,
             is_lurked)
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
    sql = """INSERT INTO yxp_project.paper_audit_question_attribute (  
                id,
                paper_audit_question_id,
                attribute_code, 
                check_content,
                updated_content,
                is_report_error,
                is_checked,
                is_knowledge_error,
                child_question_number,
                main_question,
                created,
                updated,
                is_lurked
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
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
