"""
@project:py_autotest
@filename:g_user_purchasing.py
@create_time:2021/6/16/0016 11:02
@Author:duzhengjun
@detail:Don't stop learning!!!
@Motto:Sow nothing, reap nothing
"""
import random
import sys
import time
from datetime import datetime
import pymysql
from faker import Faker

import hashlib

conn = ""
cur = ""

records = []
count = 20

# 字符串生成md5的方法
def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    # print(m.hexdigest())
    return m.hexdigest()

# 构造插入数据
def gen_data(count):
    global records
    # 指定中文
    f = Faker("zh_CN")
    for i in range(count):

        #  `id` bigint(0) UNSIGNED NOT NULL AUTO_INCREMENT
        id = 20010+i

        # `user_id` bigint(0) UNSIGNED NOT NULL DEFAULT 0 COMMENT '用户id'
        # user_id = int(f.random.randint(0, 10000000000000))
        user_id = 10385+i

        # `mobile` varchar(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '注册电话'
        mobile = f.phone_number()


        # `experience_num` int(0) UNSIGNED NOT NULL DEFAULT 0 COMMENT '用户经验值'
        experience_num = 0

        # `total_money` decimal(10, 2) UNSIGNED NOT NULL COMMENT '用户总消费金额'
        total_money = 0.00

        # `total_number` int(0) UNSIGNED NOT NULL DEFAULT 0 COMMENT '总消费次数'
        total_number = 0

        # `avg_money` decimal(10, 2) UNSIGNED NOT NULL COMMENT '平均每单费金额',
        avg_money = 0.00

        # `product_class` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '所有购买商品的所有分类，
        # \r\n用逗号隔开：,2,3,33,44,',
        product_class = ",1,2"

        # `user_label` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '用户的所有标签，\r\n用逗号隔开：,2,3,33,44,'
        user_label = ",1,3,4"

        # `user_status` tinyint(0) UNSIGNED NOT NULL DEFAULT 1 COMMENT '用户状态 1正常 0禁用',
        user_status = 1

        # `last_order_time` timestamp(0) NULL DEFAULT NULL COMMENT '最后消费时间',
        last_order_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #  `create_time` timestamp(0) NULL DEFAULT NULL COMMENT '创建时间'
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # `update_time` timestamp(0) NULL DEFAULT NULL COMMENT '更新时间'
        update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # `data_state` enum('invalid','normal') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT
        # 'normal' COMMENT '数据状态，normal：正常，invalid：无效',
        data_state = "normal"

        r = (id, user_id, mobile, experience_num, total_money, total_number, avg_money, product_class, user_label, user_status, last_order_time,
             create_time, update_time, data_state)
        records.append(r)
        print(r)


start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
gen_data(count)


try:
    # 创建一个数据库连接
    conn = pymysql.connect(
        host='118.31.17.237',
        port=3306,
        user='bearer',
        passwd='eLRF8Iev5RQi',
        db='dev',
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
    sql = """INSERT INTO dev.g_user_purchasing (  
                id,
                user_id, 
                mobile, 
                experience_num,
                total_money,
                total_number,
                avg_money,
                product_class,
                user_label,
                user_status,
                last_order_time,
                create_time,
                update_time,
                data_state
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