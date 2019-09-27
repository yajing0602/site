import pymysql
mysql_info = {"host": 'dls.test',
              "port": 3306,
              "user": 'root',
              "passwd": 'dls123456',
              "db": 'celery',
              "charset": 'utf8'}
class MysqlUtil():
    '''
    mysql 数据库相关操作连接数据库信息：mysql_info 创建游标：mysql_execute
    查询某个字段对应的字符串：mysql_getstring 查询一组数据：mysql_getrows
    关闭 mysql 连接：mysql_close'''
    def __init__(self):
        self.db_info =mysql_info
        u'''连接池方式'''
        self.conn = MysqlUtil.getConnect(self.db_info)
    @staticmethod
    def getConnect(db_info):
        '''静态方法，从连接池中取出连接'''
        try:
            conn = pymysql.connect(host=db_info['host'],
            port=db_info['port'],
            user=db_info['user'],
            passwd=db_info['passwd'],
            db=db_info['db'],
            charset=db_info['charset'])
            return conn
        except Exception as a:
            print("数据库连接异常：%s" % a)

    def mysql_execute(self,sql,):
        '''执行 sql 语句'''
        cur=self.conn.cursor()
        try:
            cur.execute(sql)
        except Exception as a:
            self.conn.rollback()  # sql 执行异常后回滚
            print("执行 SQL 语句出现异常：%s" % a)
        else:
            cur.close()
            self.conn.commit()  # sql 无异常时提交

    def mysql_getrows(self,sql):
        ''' 返回查询结果'''

        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except Exception as a:
            print("执行 SQL 语句出现异常：%s" % a)
        else:
            rows = cur.fetchall()
            cur.close()
            return rows

    def mysql_getstring(self,sql):
        '''查询某个字段的对应值'''

        rows = self.mysql_getrows(sql)
        if rows != None:
            for row in rows:
                for i in row:
                    return i

    def mysql_close(self):
        ''' 关闭 close mysql'''

        try:
            self.conn.close()
        except Exception as a:
            print("数据库关闭时异常：%s" % a)
# MySQLdb.connect() 建立数据库连接
# cur = conn.cursor() #通过获取到的数据库连接 conn 下的 cursor()方法
# 来创建游标。
# cur.execute() #过游标 cur 操作 execute()方法可以写入纯 sql 语句。通过execute()方法中写如sql语句来对数据进行操作。
# cur.close() # cur.close() 关闭游标
# conn.commit() # conn.commit()方法在提交事物，在向数据库插入(或update)一条数据时必须要有这个方法，否则数据不会被真正的插入。
# conn.rollback() # 发生错误时候回滚
# conn.close() # Conn.close()关闭数据库连接
if __name__ == "__main__":
    mysql=MysqlUtil()
    sql = "SELECT course_schedule_id FROM course_schedule_relation As A ,course_schedule As B  WHERE A.course_id='2583' and  B.name='course_6' and A.course_schedule_id = B.id"
    # mysql.mysql_execute(sql)
    # # print
    # rows=mysql.mysql_getrows(sql)
    # print(rows)
    data=mysql.mysql_getstring(sql)
    print(data)
    mysql.mysql_close()