import mysql.connector


def getDatabase():
    return mysql.connector.connect(host="localhost", user="root", passwd="root", db="dev6")