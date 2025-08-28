"""
里边主要放一些公共方法，例如faker，或者连接数据库
"""
from faker import Faker
import pymysql
import traceback

#faker方法
def get_info(i):
    faker = Faker(locale='zh-cn')
    if i == "名字":
        return faker.name()
    elif i == "地址":
        return faker.address()
    elif i == "身份证号":
        return faker.ssn(min_age = 18 , max_age = 95)


#连接数据库
class DB:
    def __init__(self,user,password,database,host):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
    def connect(self):
        #创建数据库对象
        self.db = pymysql.connect(host=self.host,user=self.user,password=self.password,
                                  database=self.database,cursorclass=pymysql.cursors.DictCursor)

        #创建游标
        self.cursor = self.db.cursor()

    def close(self):
        #先关闭游标
        self.cursor.close()
        #再关闭数据库
        self.db.close()

    #查找符合条件的一条数据
    def Search_One(self,sql):
        result = None
        self.connect()  #连接数据库
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            return result
        except:
            traceback.print_exc()   #错误的信息打印在控制台
            self.db.rollback()  #发生异常数据库回滚
            return result
        finally:
            self.close()

    #查找符合条件的多条数据
    def Search_All(self,sql):
        result = None
        self.connect()  #连接数据库
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except:
            traceback.print_exc()
            self.db.rollback()
            return result
        finally:
            self.close()

    #主操作,增删改查都用这个方法
    def __edit(self,sql):
        self.connect()
        try:
            self.cursor.execute(sql)    #先去执行sql
            self.db.commit()
            return 1
        except:
            self.db.rollback()
            traceback.print_exc()   #打印错误信息
            return 0
        finally:
            self.close()

    def insert(self,sql):
        return self.__edit(sql)

    def delete(self,sql):
        return self.__edit(sql)
    def update(self,sql):
        return self.__edit(sql)



















