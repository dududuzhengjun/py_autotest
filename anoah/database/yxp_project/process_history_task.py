# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：process_history_task
@Author: duzhengjun
@create_time：2020/6/17 20:02
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
count = 999267


# 构造插入数据
def gen_data(count):
    global records
    f = Faker("zh_cn")
    for i in range(count):
        # `task_id` bigint(20) unsigned NOT NULL,
        task_id = 1255380573753548803 + i

        #   `process_define_id` bigint(20) unsigned DEFAULT NULL,
        process_define_id_list = [1, 2]
        process_define_id = random.choice(process_define_id_list)

        #   `process_instance_id` bigint(20) unsigned DEFAULT NULL,
        process_instance_id = 1255380471735402500 + i

        #   `execution_id` bigint(20) unsigned DEFAULT NULL,
        execution_id = int(f.random.randint(1, 10))

        #   `action_name` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '节点名称',
        action_name_list = ("习题录入", "习题检查", "修改错题", "发起审核任务", "发起录入任务", "埋错检查", "审核任务初始", "审核试题"
                            , "审核通过", "录入任务初始", "检查埋错", "检查审核", "结束", "试题埋错")
        action_name = random.choice(action_name_list)

        #   `action_code` varchar(50) COLLATE utf8_bin DEFAULT NULL COMMENT '节点操作',
        action_code_list = ("00", "10", "20", "30", "40", "50", "60", "70"
                            , "80", "90")
        action_code = random.choice(action_code_list)

        #   `operation` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '操作',
        operation_list = ["创建", "发布", "提交", "结束", "转交", "退回"]
        operation = random.choice(operation_list)

        #   `operation_code` varchar(50) COLLATE utf8_bin DEFAULT NULL COMMENT '操作码',
        operation_code_list = ("00", "10", "20", "30", "40", "50", "60", "70"
                               , "80", "90")
        operation_code = random.choice(operation_code_list)

        #   `description` varchar(4000) COLLATE utf8_bin DEFAULT NULL,
        description = str(f.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))

        #   `assignee` bigint(20) unsigned DEFAULT NULL COMMENT '节点签收人',
        assignee = int(f.random.randint(1, 100000))

        #   `assignee_name` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '签收人姓名',
        assignee_name = str(f.name())

        #   `start_time` datetime(3) NOT NULL,
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #   `end_time` datetime(3) DEFAULT NULL,
        end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #   `delete_reason` varchar(4000) COLLATE utf8_bin DEFAULT NULL,
        delete_reason = str(f.sentence(nb_words=5, variable_nb_words=True, ext_word_list=None))

        #   `due_date` datetime(3) DEFAULT NULL,
        due_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #   `created` datetime NOT NULL,
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #   `updated` datetime NOT NULL,
        updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #   `audit_num` int(3) unsigned DEFAULT '1' COMMENT '审核次数',
        audit_num = int(f.random.randint(0, 10))


        r = (task_id,
             process_define_id,
             process_instance_id,
             execution_id,
             action_name,
             action_code,
             operation,
             operation_code,
             description,
             assignee,
             assignee_name,
             start_time,
             end_time,
             delete_reason,
             due_date,
             created,
             updated,
             audit_num)
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
    sql = """INSERT INTO yxp_project.process_history_task (  
                task_id,
                process_define_id,
                process_instance_id, 
                execution_id,
                action_name,
                action_code,
                operation,
                operation_code,
                description,
                assignee,
                assignee_name,
                start_time,
                end_time,
                delete_reason,
                due_date,
                created,
                updated,
                audit_num
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
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
