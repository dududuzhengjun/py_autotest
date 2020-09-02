# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：publish_stat_resource_kp
@Author: duzhengjun
@create_time：2020/6/20 09:45
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
        # `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '序号',
        id = 612 + i

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

        # `addr_id` char(22) NOT NULL COMMENT '资源地址id',
        addr_id = str(
            f.password(
                length=22,
                special_chars=False,
                digits=True,
                upper_case=True,
                lower_case=True,
            )
        )
        # `knowledge_point_id` bigint(20) NOT NULL COMMENT '知识点ID',
        knowledge_point_id = int(f.random.randint(0, 10000))

        # `addr_pid` char(22) NOT NULL COMMENT '资源父地址id',
        addr_pid = str(
            f.password(
                length=22,
                special_chars=False,
                digits=True,
                upper_case=True,
                lower_case=True,
            )
        )

        # `resource_id` char(22) NOT NULL DEFAULT '' COMMENT '资源id',
        resource_id = str(
            f.password(
                length=22,
                special_chars=False,
                digits=True,
                upper_case=True,
                lower_case=True,
            )
        )


        # `knowledge_point_name` varchar(50) NOT NULL DEFAULT '' COMMENT '知识点名称',
        knowledge_point_name = str(f.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))

        # `student_number` int(11) NOT NULL DEFAULT '0' COMMENT '参与学生人数',
        student_number = int(f.random.randint(0, 10))

        #   `correct_rate` int(11) NOT NULL DEFAULT '-1' COMMENT '正确率(正确率*10000)',
        correct_rate = int(f.random.randint(-1, 10000))

        # `final_correct_rate` int(11) NOT NULL DEFAULT '-1' COMMENT '重做正确率(正确率*10000)',
        final_correct_rate = int(f.random.randint(-1, 10000))

        #   `created` datetime NOT NULL COMMENT '创建时间',
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #   `updated` datetime NOT NULL COMMENT '更新时间',
        updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        r = (id,
             publish_id,
             addr_id,
             knowledge_point_id,
             addr_pid,
             resource_id,
             knowledge_point_name,
             student_number,
             correct_rate,
             final_correct_rate,
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
    sql = """INSERT INTO yxp_publish.publish_stat_resource_kp (  
                id,
                publish_id,
                addr_id, 
                knowledge_point_id,
                addr_pid,
                resource_id,
                knowledge_point_name,
                student_number,
                correct_rate,
                final_correct_rate,
                created,
                updated
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
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
