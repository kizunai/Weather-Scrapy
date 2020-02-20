import pymysql
import log_mysql

def con_db():

    try:
        #连接database
        db = pymysql.connect("ip","root","root","WeatherForecast")
    except Exception:
        logger = log_mysql.MyLog("mysql", "log\\debug.log")
        logger.logger.debug("数据库连接失败")

    return db

def insert_city_data(db, city, day, switch):
    cursor = db.cursor()
    sql = chose_sql("insert", switch)

    try:
        cursor.execute(sql, [city, day])
        db.commit()
    except Exception as e:
        print(e)
        logger = log_mysql.MyLog("mysql","log\\debug.log")
        logger.logger.debug("插入"+ city +"数据错误")
        db.rollback()

    cursor.close()
    # db.close()

def select_city(db, city):
    # db = con_db()
    cursor = db.cursor()

    try:
        sql = """select * from forecast7days where city = %s"""
        cursor.execute(sql, city)
        result = cursor.fetchall()
        if len(result) != 0 :
            cursor.close()
            return 1
        else:
            cursor.close()
            return 0
    except Exception:
        logger = log_mysql.MyLog("mysql","log\\debug.log")
        logger.logger.debug("查询"+ city +"数据错误")
        db.rollback()
        cursor.close()
        return -1


def update_day(db, city, day, switch):
    # db = con_db()
    cursor = db.cursor()
    sql = chose_sql("update", switch)

    try:
        cursor.execute(sql, [day, city])
        db.commit()
    except Exception:
        logger = log_mysql.MyLog("mysql", "log\\debug.log")
        logger.logger.debug("更新" + city + "("+ switch + ")" + "数据错误")
        db.rollback()

    cursor.close()
    # db.close()


# 选择sql语句
def chose_sql(sql_type, switch):
    if sql_type == 'update':
        if switch == 1:
            sql = """update forecast7days set day_1 = %s where city = %s"""
        elif switch == 2:
            sql = """update forecast7days set day_2 = %s where city = %s"""
        elif switch == 3:
            sql = """update forecast7days set day_3 = %s where city = %s"""
        elif switch == 4:
            sql = """update forecast7days set day_4 = %s where city = %s"""
        elif switch == 5:
            sql = """update forecast7days set day_5 = %s where city = %s"""
        elif switch == 6:
            sql = """update forecast7days set day_6 = %s where city = %s"""
        elif switch == 7:
            sql = """update forecast7days set day_7 = %s where city = %s"""
    elif sql_type == 'insert':
        if switch == 1:
            sql = "insert into forecast7days(city, day_1)values(%s,%s)"
        elif switch == 2:
            sql = "insert into forecast7days(city, day_2)values(%s,%s)"
        elif switch == 3:
            sql = "insert into forecast7days(city, day_3)values(%s,%s)"
        elif switch == 4:
            sql = "insert into forecast7days(city, day_4)values(%s,%s)"
        elif switch == 5:
            sql = "insert into forecast7days(city, day_5)values(%s,%s)"
        elif switch == 6:
            sql = "insert into forecast7days(city, day_6)values(%s,%s)"
        elif switch == 7:
            sql = "insert into forecast7days(city, day_7)values(%s,%s)"

    return sql