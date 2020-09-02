# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：publish_resource_convers
@Author: duzhengjun
@create_time：2020/6/18 18:27
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
count = 1000000


# 构造插入数据
def gen_data(count):
    global records
    f = Faker("zh_cn")
    for i in range(count):
        # `id` bigint(11) NOT NULL AUTO_INCREMENT,
        id = 1255380573753548803 + i

        #   `publish_id` char(22) NOT NULL COMMENT '发布id',
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

        #   `resource_id` char(22) NOT NULL DEFAULT '' COMMENT '资源id',
        resource_id = str(
            f.password(
                length=22,
                special_chars=False,
                digits=True,
                upper_case=True,
                lower_case=True,
            )
        )

        #   `conversion_status` tinyint(2) NOT NULL COMMENT '转换状态  0-未转换，1-转换成功，2-转换失败',
        conversion_status_list = [0, 1, 2]
        conversion_status = random.choice(conversion_status_list)

        #   `created` datetime NOT NULL COMMENT '本条数据创建时间',
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #   `updated` datetime NOT NULL COMMENT '本条数据更新时间',
        updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        r = (id,
             publish_id,
             addr_id,
             resource_id,
             conversion_status,
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
    sql = """INSERT INTO yxp_publish.publish_resource_convers (  
                id,
                publish_id,
                addr_id, 
                resource_id,
                conversion_status,
                created,
                updated
            ) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
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
