import pymysql
import re

# 连接数据库
# db = pymysql.connect(host='localhost',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      database='yin',
#                      charset='utf8')
# 生成游标对象（操作数据库，执行SQL语句，获取结果）
# cur = db.cursor()
# ---------------执行各种SQL操作------------------
# 插入
# try:
#     sql ="insert into Class (name,age,score)" \
#          "values (%s,%s,%s);"
#     cur.execute(sql,['ton',17,98])
#     db.commit()#同步到数据库
# except Exception:
#     db.rollback()#数据回复操作之前
# try:
#     sql = "insert into Class (name,age,sex,score)" \
#           "values (%s,%s,%s,%s);"
#     meg = [('Dave', 17, 'm', 81), ('Ala', 18, 'w', 84), ('Eva', 19, 'w', 91)]
#     # for i in meg:
#     #     cur.execute(sql, i)
#     cur.executemany(sql,meg)
#     db.commit()
# except:
#     db.rollback()
#     print('错了')

# 读
# sql='select name ,age,score from Class;'
# cur.execute(sql)
# 结果1
# for i in cur:
#     print(i)
# 结果2
# one_row = cur.fetchone()
# print(one_row)
# 获取多条记录
# many_row=cur.fetchmany(3)
# print(many_row)
# 获取所有记录
# all_row =cur.fetchall()
# print(all_row)
# name=input('请输入一个姓名:')
# sg="select attack,count from sanguo where name=%s;"#无论什么类型都是%s
# cur.execute(sg,[name])
# print(cur.fetchone())
# 关闭游标和数据库连接
# cur.close()
# db.close()
# def add_word():
#     id=1
#     word = open("/home/tarena/桌面/dict.txt", 'r')
#     db = pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='dict',charset='utf8')
#     cur = db.cursor()
#     try:
#         sql ="insert into dict_word values (%s,%s,%s)"
#         while True:
#             word1 = word.readline()
#             if not word1:
#                 break
#             word1=word1.split(' ', 1)
#             word1[1] = word1[1].replace('\n', '').lstrip()
#             cur.execute(sql,[id,word1[0],word1[1]])
#             id += 1
#         db.commit()
#         print('对了')
#     except Exception as s:
#         db.rollback()
#         print(s)
#     cur.close()
#     db.close()
#
# add_word()


# db = pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='yin',charset='utf8')
# cur = db.cursor()
# with open('/home/tarena/桌面/meinv.jpg','rb') as f:
#     data=f.read()
# try:
#     sql="updata Class set image=%s where name ='wz';"
#     cur.execute(sql,[data])
#     db.commit()
# except:
#     db.rollback()
# cur.close()
# db.close()