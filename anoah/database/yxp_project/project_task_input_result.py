# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：project_task_input_result
@Author: duzhengjun
@create_time：2020/6/17 18:36
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
        # `id` bigint(20) unsigned NOT NULL,
        id = 1245019270761451523+i

        #   `is_valid` tinyint(2) DEFAULT '0' COMMENT '是否有效,0-无效,1-有效',
        is_valid_list = [0, 1]
        is_valid = random.choice(is_valid_list)

        #   `task_id` bigint(20) DEFAULT NULL COMMENT 'project_task,ID 录入任务ID',
        task_id = 1234401616312963074+i

        #   `process_instance_id` bigint(20) DEFAULT NULL,
        process_instance_id = 1236850902460030979+i

        #   `knowledge_error_rate` decimal(10,2) DEFAULT NULL COMMENT '知识性出错概率',
        knowledge_error_rate = int(f.random.randint(0, 100)) % 100

        #   `audit_question_num` tinyint(4) DEFAULT '0' COMMENT '录入任务审核题数',
        audit_question_num = int(f.random.randint(1, 100))

        #   `import_question_num` tinyint(4) unsigned DEFAULT '0' COMMENT '录入任务题数',
        import_question_num = int(f.random.randint(1, 100))

        #   `audit_num` int(11) unsigned DEFAULT '0' COMMENT '审核次数',
        audit_num = int(f.random.randint(1, 100))

        #   `statistics_month` varchar(12) DEFAULT NULL COMMENT '统计月份',
        statistics_month = int(f.random.randint(1, 12))

        #   `created` datetime NOT NULL,
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #   `updated` datetime NOT NULL,
        updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        r = (id,
             is_valid,
             task_id,
             process_instance_id,
             knowledge_error_rate,
             audit_question_num,
             import_question_num,
             audit_num,
             statistics_month,
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
    sql = """INSERT INTO yxp_project.project_task_input_result (  
                id,
                is_valid,
                task_id, 
                process_instance_id,
                knowledge_error_rate,
                audit_question_num,
                import_question_num,
                audit_num,
                statistics_month,
                created,
                updated
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
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
