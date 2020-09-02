# -*- coding:utf-8 -*- 
"""
@project: youxueketang
@filename：project_task_required
@Author: duzhengjun
@create_time：2020/6/17 13:26
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

        # `id` bigint(20) unsigned NOT NULL
        id = 1255380573229170690+i

        # `task_id` bigint(20) NOT NULL COMMENT 'project_task表ID'
        task_id = 1255380471735402498 + i

        #   `task_type` varchar(50) DEFAULT NULL COMMENT '任务类型 base_data_dictionary.type=TASK_TYPE'
        task_type_list = [1, 2]
        task_type = random.choice(task_type_list)

        #   `required_type` varchar(50) DEFAULT NULL COMMENT 'base_data_dictionary.type=REQUIRED_TYPE'
        required_type_list = [0, 1, 2]
        required_type = random.choice(required_type_list)

        #   `answer` tinyint(2) unsigned DEFAULT '0' COMMENT '答案'
        answer_list = [0, 1]
        answer = random.choice(answer_list)

        #   `prompt` tinyint(2) unsigned DEFAULT '0' COMMENT '提示'
        prompt_list = [0, 1]
        prompt = random.choice(prompt_list)

        #   `explanation` tinyint(2) unsigned DEFAULT '0' COMMENT '解析'
        explanation_list = [0, 1]
        explanation = random.choice(explanation_list)

        #   `comment` tinyint(2) unsigned DEFAULT '0' COMMENT '点评'
        comment_list = [0, 1]
        comment = random.choice(comment_list)

        #   `knowledge_point` tinyint(2) unsigned DEFAULT '0' COMMENT '知识点'
        knowledge_point_list = [0, 1]
        knowledge_point = random.choice(knowledge_point_list)

        #   `difficulty` tinyint(2) unsigned DEFAULT '0' COMMENT '难易度'
        difficulty_list = [0, 1]
        difficulty = random.choice(difficulty_list)

        #   `tag` tinyint(2) DEFAULT '0'
        tag_list = [0, 1]
        tag = random.choice(tag_list)

        #   `time_consume` tinyint(2) unsigned DEFAULT '0' COMMENT '耗时'
        time_consume_list = [0, 1]
        time_consume = random.choice(time_consume_list)

        #   `awareness` tinyint(2) unsigned DEFAULT '0' COMMENT '认知度'
        awareness_list = [0, 1]
        awareness = random.choice(awareness_list)

        #   `skill` tinyint(2) unsigned DEFAULT '0' COMMENT '技能'
        skill_list = [0, 1]
        skill = random.choice(skill_list)

        #   `ability` tinyint(2) unsigned DEFAULT '0' COMMENT '能力'
        ability_list = [0, 1]
        ability = random.choice(ability_list)

        #   `application_scenario` tinyint(2) unsigned DEFAULT '0' COMMENT '应用场景'
        application_scenario_list = [0, 1]
        application_scenario = random.choice(application_scenario_list)

        #   `stars` tinyint(2) unsigned DEFAULT '0' COMMENT '推荐指数'
        stars_list = [0, 1]
        stars = random.choice(stars_list)

        #   `resource_source` tinyint(2) unsigned DEFAULT '0' COMMENT '资源来源'
        resource_source_list = [0, 1]
        resource_source = random.choice(resource_source_list)

        #   `body` tinyint(2) unsigned DEFAULT '0' COMMENT '内容'
        body_list = [0, 1]
        body = random.choice(body_list)

        #   `tip` tinyint(2) unsigned DEFAULT '0' COMMENT '提示'
        tip_list = [0, 1]
        tip = random.choice(tip_list)

        #   `thematic` tinyint(2) unsigned DEFAULT '0'
        thematic_list = [0, 1]
        thematic = random.choice(thematic_list)

        #   `assistant` tinyint(2) unsigned DEFAULT '0'
        assistant_list = [0, 1]
        assistant = random.choice(assistant_list)

        #   `textbook` tinyint(2) unsigned DEFAULT '0'
        textbook_list = [0, 1]
        textbook = random.choice(textbook_list)


        r = (id, task_id, task_type, required_type, answer, prompt, explanation, comment, knowledge_point, difficulty,
             tag, time_consume, awareness, skill, ability, application_scenario, stars, resource_source, body, tip, thematic, assistant, textbook)
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
    sql = """INSERT INTO yxp_project.project_task_required (  
                id,
                task_id, 
                task_type, 
                required_type,
                answer,
                prompt,
                explanation,
                comment,
                knowledge_point,
                difficulty,
                tag,
                time_consume,
                awareness,
                skill,
                ability,
                application_scenario,
                stars,
                resource_source,
                body,
                tip,
                thematic,
                assistant,
                textbook
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
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