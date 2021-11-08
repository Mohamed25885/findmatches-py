import mysql.connector
from mysql.connector import Error

#redirecting to parent directory
from os import path
from sys import path as sysPath
p = path.abspath('.')
sysPath.insert(1, p)
  
# importing
import constant

try:
    connection = mysql.connector.connect(
    host=constant.dbHost,
    user=constant.dbUser,
    password=constant.dbPassword,
    database = constant.dbName)

    if connection.is_connected():
        cursor = connection.cursor()
except Error as e:
    print(e)
    exit()