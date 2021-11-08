import initDB
from initDB import constant

initDB.cursor.execute("USE {}".format(constant.dbName))

def tryIfConnected(funToLoad):
    try:
        if initDB.connection.is_connected():
            funToLoad
        else:
            print("ERROR")
            exit()
    except initDB.Error as e:
        print(e)

def buildQuery(query):
    try:
        initDB.cursor.execute(query)
        initDB.connection.commit()
    except initDB.Error as e:
        print(e)

def dropTable(table):
    try:
        initDB.cursor.execute("DROP TABLE {}".format(table))
        initDB.connection.commit()
    except initDB.Error as e:
        print(e)


def insertIntoScore(name,time, level):
    #sql = "REPLACE INTO score(name, time) VALUES (%s,%s)"
    sql = '''INSERT INTO scores(name, time, level) VALUES (%s,%s, %s)
    ON DUPLICATE KEY UPDATE name = %s, time = %s, level =%s'''
    val = (name, time, level)*2
    print(val)
    try:
        initDB.cursor.execute(sql, val)
        initDB.connection.commit()
    except initDB.Error as e:
        print(e)

def getLevel(level = 1):
    sql = "SELECT name,time,level FROM scores WHERE level = %s ORDER BY time"
    initDB.cursor.execute(sql, (level,))
    return initDB.cursor.fetchall()
        