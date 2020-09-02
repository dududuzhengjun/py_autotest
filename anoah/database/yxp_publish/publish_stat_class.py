# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：publish_stat_class
@Author: duzhengjun
@create_time：2020/6/19 12:06
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
count = 10


# 构造插入数据
def gen_data(count):
    global records
    f = Faker("zh_cn")
    for i in range(count):
        # `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '序号',
        id = 999991 + i

        #   `publish_id` char(22) NOT NULL DEFAULT '' COMMENT '发布id'
        publish_id = str(
            f.password(
                length=22,
                special_chars=False,
                digits=True,
                upper_case=True,
                lower_case=True,
            )
        )

        #   `addr_id` char(22) NOT NULL COMMENT '地址id',
        addr_id = str(
            f.password(
                length=22,
                special_chars=False,
                digits=True,
                upper_case=True,
                lower_case=True,
            )
        )

        #   `correct_rate` int(11) NOT NULL DEFAULT '-1' COMMENT '正确率(正确率*10000)',
        correct_rate = int(f.random.randint(-1, 10000))

        # `finished_counter` int(11) NOT NULL DEFAULT '0' COMMENT '完成人数',
        finished_counter = int(f.random.randint(0, 10))

        # `corrected_counter` int(11) NOT NULL DEFAULT '0' COMMENT '已批改人数',
        corrected_counter = int(f.random.randint(0, finished_counter))

        # `uncorrected_counter` int(11) NOT NULL DEFAULT '0' COMMENT '待批改人数',
        uncorrected_counter = finished_counter-corrected_counter

        # `final_correct_rate` int(11) NOT NULL DEFAULT '-1' COMMENT '重做正确率(正确率*10000)',
        final_correct_rate = int(f.random.randint(-1, 10000))

        # `final_corrected_counter` int(11) NOT NULL DEFAULT '0' COMMENT '重做已批改人数',
        final_corrected_counter = int(f.random.randint(0, corrected_counter))

        # `final_uncorrected_counter` int(11) NOT NULL DEFAULT '0' COMMENT '重做待批改人数',
        final_uncorrected_counter = corrected_counter-final_corrected_counter

        # `complex_uncorrected_counter` int(11) NOT NULL DEFAULT '0' COMMENT '复合未批改人数 (首次未批改或者重做未批改)',
        complex_uncorrected_counter = final_uncorrected_counter

        # `good_answer_counter` int(11) NOT NULL DEFAULT '0' COMMENT '节点班级优秀答案数量(不区分首次或重做)',
        good_answer_counter = final_corrected_counter


        #   `created` datetime NOT NULL COMMENT '创建时间',
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #   `updated` datetime NOT NULL COMMENT '更新时间',
        updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        r = (id,
             publish_id,
             addr_id,
             correct_rate,
             finished_counter,
             corrected_counter,
             uncorrected_counter,
             final_correct_rate,
             final_corrected_counter,
             final_uncorrected_counter,
             complex_uncorrected_counter,
             good_answer_counter,
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
    sql = """INSERT INTO yxp_publish.publish_stat_class (  
                id,
                publish_id,
                addr_id, 
                correct_rate,
                finished_counter,
                corrected_counter,
                uncorrected_counter,
                final_correct_rate,
                final_corrected_counter,
                final_uncorrected_counter,
                complex_uncorrected_counter,
                good_answer_counter,
                created,
                updated
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
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
