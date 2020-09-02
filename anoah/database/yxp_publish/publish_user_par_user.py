# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：publish_user_par_user
@Author: duzhengjun
@create_time：2020/6/20 13:29
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
        id = 22437 + i

        # `user_id` char(22) NOT NULL COMMENT '用户id',
        user_id = int(f.random.randint(1, 10000))

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

        # `org_id` bigint(20) NOT NULL COMMENT '机构id',
        org_id_list = [1148510848570884097, 1156461337077878785]
        org_id = random.choice(org_id_list)

        # `class_id` char(22) NOT NULL COMMENT '班级id',
        class_id_list = [1148515711648350209, 1153854541125468161, 1247479276194795521]
        class_id = random.choice(class_id_list)

        # `subject_id` int(11) NOT NULL DEFAULT '0' COMMENT '科目id',
        subject_id = int(f.random.randint(1, 3))

        # `status` int(4) NOT NULL DEFAULT '0' COMMENT '作业状态 20未完成 30待批改 40批改完   120未完成删除 130待批改删除 140已批改删除  ps:删除状态=原来状态值+100',
        status_list = [10, 20, 30, 40, 120, 130, 140]
        status = random.choice(status_list)

        # `final_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '重做状态 10无重做 20重做未完成 30重做已完成',
        final_status_list = [10, 20, 30]
        final_status = random.choice(final_status_list)

        # `revise_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '作业的订正状态 \r\n0 无需订正(没有试题错误 即作业正确率为100, 或作业资源均为学习类) \r\n1 已订正(所有试题已提交订正 并且所有客观题订正后的正确率为100)\r\n2 未订正(有客观题订正后的正确率不为100 或有主观题 未提交订正)',
        revise_status_list = [0, 1, 2]
        revise_status = random.choice(revise_status_list)

        # `start_time` datetime NOT NULL COMMENT '作业开始时间',
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # `deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT '删除标记 10未删除 20已删除',
        deleted_list = [10, 20]
        deleted = random.choice(deleted_list)

        #   `created` datetime NOT NULL COMMENT '创建时间',
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #   `updated` datetime NOT NULL COMMENT '更新时间',
        updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        r = (id,
             user_id,
             publish_id,
             org_id,
             class_id,
             subject_id,
             status,
             final_status,
             revise_status,
             start_time,
             deleted,
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
    sql = """INSERT INTO yxp_publish.publish_user_par_user (  
                id,
                user_id,
                publish_id,
                org_id,
                class_id,
                subject_id,
                status,
                final_status,
                revise_status,
                start_time,
                deleted,
                created,
                updated
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
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
