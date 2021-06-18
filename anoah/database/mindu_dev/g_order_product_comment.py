"""
@project:py_autotest
@filename:g_order_product_comment.py
@create_time:2021/6/18/ 15:27
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
count = 50

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

        #  `id` bigint(0) UNSIGNED NOT NULL AUTO_INCREMENT,
        id = 4032+i

        # `user_id` bigint(0) NOT NULL DEFAULT 0 COMMENT '评论的user',
        user_id = 29337

        # `order_product_id` bigint(0) UNSIGNED NOT NULL DEFAULT 0 COMMENT '被评论的订单商品id',
        order_product_id = 20429

        # `product_id` bigint(0) NOT NULL COMMENT '商品id'
        product_id = 2476

        # `content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '内容'
        # 随机短语
        content = str(f.sentence(nb_words=50, variable_nb_words=True, ext_word_list=None))

        # `score` decimal(2, 1) NOT NULL COMMENT '评分'
        score = int(f.random.randint(1, 5))

        # `pid` bigint(0) NOT NULL DEFAULT 0 COMMENT '主评论id',
        pid = 0

        # `rid` bigint(0) UNSIGNED NOT NULL DEFAULT 0 COMMENT '回复的评论id',
        rid = 0

        # `support` int(0) UNSIGNED NOT NULL DEFAULT 0 COMMENT '点赞数',
        support = 0

        # `hate` int(0) UNSIGNED NOT NULL DEFAULT 0 COMMENT '点踩数',
        hate = 0

        #  `create_time` timestamp(0) NULL DEFAULT NULL COMMENT '创建时间'
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # `update_time` timestamp(0) NULL DEFAULT NULL COMMENT '更新时间'
        update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # `data_state` enum('invalid','normal') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT
        # 'normal' COMMENT '数据状态，normal：正常，invalid：无效',
        data_state = "normal"

        # `b_user_id` bigint(0) UNSIGNED NOT NULL DEFAULT 0 COMMENT '被评论的user',
        b_user_id = 0

        # `img_url` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '订单商品评论图片路径多张 , 隔开',
        img_url = "product/14057860336055787520.png,product/14057860336055787522.png,product/14057860336055787521.png"

        r = (id, user_id, order_product_id, product_id, content, score, pid, rid, support, hate,
             create_time, update_time, data_state, b_user_id, img_url)
        records.append(r)
        # print(r)


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
    )

    # 创建一个游标对象
    cursor = conn.cursor()
except Exception:
    print("数据库连接失败")
    sys.exit()

sql = ""
try:
    # 批量执行SQL语句
    sql = """INSERT INTO css_sg.g_order_product_comment (  
                id,
                user_id, 
                order_product_id, 
                product_id,
                content,
                score,
                pid,
                rid,
                support,
                hate,
                create_time,
                update_time,
                data_state,
                b_user_id,
                img_url
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