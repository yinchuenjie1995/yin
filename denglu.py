import pymysql

class Database:
    def __init__(self):
        pass
    def connect_msq(self):
        db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='yin',
                             charset='utf8')