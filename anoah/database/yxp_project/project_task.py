# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：project_task
@Author: duzhengjun
@create_time：2020/6/16 11:50
@detail：Don't stop learning!!!
@Motto：Sow nothing, reap nothing
"""
import random
import sys
import time
import pymysql
from datetime import datetime
import uuid
import faker

conn = ""
cur = ""

records = []
count = 0

# 构造插入数据
def gen_data(count):
    global records
    f = faker.Faker("zh_cn")
    for i in range(count):

        # `task_id` bigint(20) unsigned NOT NULL
        task_id = 1255380471735402509+i

        # `project_id` bigint(20) unsigned DEFAULT NULL COMMENT '项目ID'
        project_id = 1251093992435630093+i

        # `task_type` varchar(50) DEFAULT NULL COMMENT '任务类型 base_data_dictionary.type=TASK_TYPE'
        task_type_list = ['1', '2']
        task_type = random.choice(task_type_list)

        # `process_instance_id` bigint(20) DEFAULT NULL COMMENT '流程任务实例'
        process_instance_id = 1255380471735402510+i

        # `name` varchar(50) DEFAULT NULL COMMENT '名称'
        name = str(f.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))

        # `start_time` datetime DEFAULT NULL COMMENT '开始时间'
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # `end_time` datetime DEFAULT NULL COMMENT '结束时间'
        end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # `creator` int(11) unsigned DEFAULT NULL COMMENT '创建者'
        creator = int(f.random.randint(0, 10000))

        # `creator_name` varchar(255) DEFAULT NULL COMMENT '创建者姓名'
        creator_name_list = ['杜征骏', '赵小平', '徐嘉', '蒋勇', 'admin', '董俊良']
        creator_name = random.choice(creator_name_list)

        # `period_id` int(11) DEFAULT NULL COMMENT '学段,继承项目'
        period_id_list = ['1', '2', '3']
        period_id = random.choice(period_id_list)

        # `subject_id` int(11) DEFAULT NULL COMMENT '科目,继承项目'
        subject_id_list = ['1', '2', '3']
        subject_id = random.choice(subject_id_list)

        # `data_address` varchar(500) DEFAULT NULL COMMENT '资料地址'
        data_address = str(f.address())

        # `is_deleted` tinyint(2) unsigned DEFAULT '0'
        is_deleted_list = ['0', '1']
        is_deleted = random.choice(is_deleted_list)

        # `scheme_type` varchar(50) NOT NULL COMMENT 'base_data_dictionary.type=SCHEME_TYPE'
        scheme_type_list = ['1', '2', '3']
        scheme_type = random.choice(scheme_type_list)

        # `scheme_id` bigint(20) DEFAULT NULL
        scheme_id = 1254289308677554188+i

        # `input_num` decimal(10,2) DEFAULT NULL COMMENT '输入的数字,与schema_type结合使用'
        input_num = int(f.random.randint(0, 100)) % 100

        # `source_type` varchar(50) NOT NULL COMMENT 'base_data_dictionary.type=SOURCE_TYPE'
        source_type_list = ['1', '2', '3']
        source_type = random.choice(source_type_list)

        # `source_name` varchar(255) DEFAULT NULL COMMENT '知识库资料名称'
        source_name = str(f.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None) + "教辅")

        # `source_id` int(11) NOT NULL COMMENT '知识库表ID,继承项目'
        source_id = int(f.random.randint(0, 50))

        # `org_id` bigint(20) unsigned DEFAULT NULL COMMENT '发布单位'
        org_id = 1

        # `org_name` varchar(255) DEFAULT NULL COMMENT '发布单位名字'
        org_name = "优学派"

        # `remark` varchar(255) DEFAULT NULL COMMENT '备注'
        remark = name+"的备注"

        # `created` datetime NOT NULL
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # `updated` datetime NOT NULL
        updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


        r = (task_id, project_id, task_type, process_instance_id, name, start_time, end_time, creator, creator_name, period_id,
             subject_id, data_address, is_deleted, scheme_type, scheme_id, input_num, source_type, source_name, source_id, org_id, org_name, remark, created, updated)
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
    sql = """INSERT INTO yxp_project.project_task (  
                task_id,
                project_id, 
                task_type, 
                process_instance_id,
                name,
                start_time,
                end_time,
                creator,
                creator_name,
                period_id,
                subject_id,
                data_address,
                is_deleted,
                scheme_type,
                scheme_id,
                input_num,
                source_type,
                source_name,
                source_id,
                org_id,
                org_name,
                remark,
                created,
                updated
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.executemany(sql, records)
    conn.commit()
except:
    print("数据插入时发生错误")

finally:
    cursor.close()  # 关闭游标
    conn.close()  # 释放连接

end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print("开始时间: " + start_time)
print("完成时间：" + end_time)