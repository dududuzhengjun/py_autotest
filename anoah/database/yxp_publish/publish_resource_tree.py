# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：publish_resource_tree
@Author: duzhengjun
@create_time：2020/6/19 09:11
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
        # `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '序号'
        id = 17692+i

        #   `publish_id` char(22) CHARACTER SET utf8 NOT NULL COMMENT '发布id',
        publish_id = str(
            f.password(
                length=22,
                special_chars=False,
                digits=True,
                upper_case=True,
                lower_case=True,
            )
        )

        #   `addr_id` char(22) CHARACTER SET utf8 NOT NULL COMMENT '地址id',
        addr_id = str(
            f.password(
                length=22,
                special_chars=False,
                digits=True,
                upper_case=True,
                lower_case=True,
            )
        )

        #   `addr_pid` char(22) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '父地址id',
        addr_pid = str(
            f.password(
                length=22,
                special_chars=False,
                digits=True,
                upper_case=True,
                lower_case=True,
            )
        )

        # `addr` text CHARACTER SET utf8 NOT NULL COMMENT '详细地址',
        addr = str(
            f.password(
                length=22,
                special_chars=False,
                digits=True,
                upper_case=True,
                lower_case=True,
            )+","+f.password(
                length=43,
                special_chars=False,
                digits=True,
                upper_case=True,
                lower_case=True,
            )
        )

        # `link_id` char(32) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '节点之间的关系id',
        link_id = str(
            f.password(
                length=22,
                special_chars=False,
                digits=True,
                upper_case=True,
                lower_case=True,
            )
        )

        # `resource_id` char(22) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '资源id',
        resource_id = str(
            f.password(
                length=22,
                special_chars=False,
                digits=True,
                upper_case=True,
                lower_case=True,
            )
        )

        # `icom_id` int(11) NOT NULL DEFAULT '0' COMMENT '播放器id',
        icom_id = 1001

        # `resource_type` char(20) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '资源类型 1.试题 2.试卷 (3.备课方案 04-25 谢兴勇增加) 4上传文件 5实体类',
        resource_type_list = ["RT1001", "RT1002"]
        resource_type = random.choice(resource_type_list)

        # `resource_type_name` char(30) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '资源类型名称',
        if resource_type == "RT1001":
            resource_type_name = "单选题"
        else:
            resource_type_name = "多选题"

        # `resource_name` char(100) NOT NULL DEFAULT '' COMMENT '资源名称',
        resource_name = "选择题"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # `resource_content` mediumtext NOT NULL COMMENT '资源内容',
        resource_content = """
        {"template":"329","answer":{"value":"A"},"extra":{"optionMode":2},"typeName":"单选题","comment":"","tip":"","contentSign":"","contentTagVersion":2,"body":{"options":[{"value":"","option":"A"},{"value":"","option":"B"},{"value":"","option":"C"},{"value":"","option":"D"}]},"explanation":"","prompt":"<img src= \"https://proj001test.anoah.com/file/download/appd883fd21fb99/screenshot/20200601/163/c_1ho2YrQZX92GVvnpIo2Zx1_20200601175754723.jpg\"/>","version":2}
        """

        # `resource_info` text NOT NULL COMMENT '资源信息 7.23 新增-王钱江',
        resource_info = """
        {"attr":{"ability":[],"applicationScene":{},"cognitiveDimension":[],"difficulty":{"id":"","name":""},"grade":{},"period":{},"recommendLevel":0,"skill":[],"subject":{}},"created":"2020-06-01 17:58:40","createdBy":{"id":"9","name":"徐嘉"},"extend":{"questionTimeConsume":0},"md5":"B595A5886DC3A2E18B89846F0FB28D08","org":{"id":"1148510848570884097","name":"白沙中学"},"resourceName":"选择题2020-06-01 17:58:40","resourceType":"RT1001","resourceTypeName":"单选题","tags":{},"updated":"2020-06-01 17:58:40","updatedBy":{"id":"9","name":"徐嘉"},"version":2}
        """

        # `children` text NOT NULL COMMENT '子节点集合',
        children = "[]"

        # `subjective_objective` tinyint(4) NOT NULL DEFAULT '0' COMMENT '主客观 0.未知；1. 主观；2. 客观',
        subjective_objective_list = [0, 1, 2]
        subjective_objective = random.choice(subjective_objective_list)

        # `should_score` decimal(12,6) NOT NULL COMMENT '标准分, "-1表示学习类资源"',
        should_score = -1.000000

        # `extra` varchar(255) NOT NULL DEFAULT '{}' COMMENT '扩展信息 默认为{} ',
        extra = "{}"

        #   `created` datetime NOT NULL COMMENT '本条数据创建时间',
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #   `updated` datetime NOT NULL COMMENT '本条数据更新时间',
        updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        r = (id,
             publish_id,
             addr_id,
             addr_pid,
             addr,
             link_id,
             resource_id,
             icom_id,
             resource_type,
             resource_type_name,
             resource_name,
             resource_content,
             resource_info,
             children,
             subjective_objective,
             should_score,
             extra,
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
    sql = """INSERT INTO yxp_publish.publish_resource_tree (  
                id,
                publish_id,
                addr_id, 
                addr_pid,
                addr,
                link_id,
                resource_id,
                icom_id,
                resource_type,
                resource_type_name,
                resource_name,
                resource_content,
                resource_info,
                children,
                subjective_objective,
                should_score,
                extra,
                created,
                updated
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
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
