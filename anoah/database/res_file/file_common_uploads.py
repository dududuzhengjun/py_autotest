# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：file_common_uploads
@Author: duzhengjun
@create_time：2020/6/13 20:02
@detail：Don't stop learning!!!
@Motto：Sow nothing, reap nothing
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
count = 0

# 字符串生成md5的方法
def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    # print(m.hexdigest())
    return m.hexdigest()

# 构造插入数据
def gen_data(count):
    global records
    f = Faker()
    for i in range(count):

        # `id` bigint(20) NOT NULL--1148504374767624193
        id = 1268456545360842760+i

        # `user_id` bigint(20) NOT NULL COMMENT '用户id'--3875
        user_id = int(f.random.randint(0, 10000000000000))

        # `file_origin_name` varchar(255) NOT NULL DEFAULT '' COMMENT '原始文件名称'--5c927216da023a90ee6d723ee0a5fcdc.jpg
        file_origin_name = str(f.file_name())


        # `file_suffix` varchar(255) NOT NULL COMMENT '文件扩展名'--jpg
        file_suffix = file_origin_name.split(".")[-1]

        # `file_size` bigint(20) NOT NULL DEFAULT '0' COMMENT '文件大小'--16310
        file_size = int(f.random.randint(0, 1000000000000))

        # `from_module` varchar(45) NOT NULL DEFAULT '' COMMENT '来源模块'
        # --record[zip]、userAvatar[jpg/png/jpeg/gif]、beikeImg[jpg/png/jpeg/gif]、beikeAudio[mp3]、beikeVideo[mp4]、beikeDoc[txt/docx/doc/pptx/ppt/xls/xlsx]

        if file_suffix == 'zip':
            from_module = "record"
        elif file_suffix == 'jpg':
            from_module = 'userAvatar'
        elif file_suffix == 'png':
            from_module = 'userAvatar'
        elif file_suffix == 'jpeg':
            from_module = 'userAvatar'
        elif file_suffix == 'gif':
            from_module = 'userAvatar'
        elif file_suffix == 'mp3':
            from_module = 'beikeAudio'
        elif file_suffix == 'mp4':
            from_module = 'beikeVideo'
        elif file_suffix == 'avy':
            from_module = 'beikeVideo'
        elif file_suffix == 'mov':
            from_module = 'beikeVideo'
        else:
            from_module = 'beikeDoc'

        # `created` datetime(3) NOT NULL ON UPDATE CURRENT_TIMESTAMP(3)--2020-05-22 12:12:31.471
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # `file_path` varchar(255) NOT NULL DEFAULT '' COMMENT '当前文件的存储路径'
        # --/app/upload/yxp-edu/appd883fd21fb99/record/20190711/22/20190711150912_3469_84v4.zip
        file_path = str("/app/upload/yxp-edu/appd883fd21fb99/record/"+from_module+f.file_path(depth=2, category=None, extension=file_suffix))

        # `file_path_md5` varchar(64) DEFAULT NULL COMMENT 'file_path的md5,file_path需要是标准的，唯一的'
        # --5cbca98b597b66fcd4068a0abe25f505
        file_path_md5 = md5(file_path)

        r = (id, user_id, file_origin_name, file_suffix, file_size, from_module, created, file_path, file_path_md5)
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
        db='res_file',
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
    sql = """INSERT INTO res_file.file_common_uploads (  
                id,
                user_id, 
                file_origin_name, 
                file_suffix,
                file_size,
                from_module,
                created,
                file_path,
                file_path_md5
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
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

