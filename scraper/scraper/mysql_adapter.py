from datetime import datetime

import mysql.connector
from mysql import connector


class MySQLAdapter():

    def getNow(self):
        now = datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')

    def connect(self, user=None, passw=None, host=None, dbname=None):
        cnx = mysql.connector.connect(user=user, password=passw, host=host,
                                      database=dbname)
        cnx.autocommit = True
        return cnx

    def closeConnection(self, cnx):
        cnx.close()

    def getExecuteSelectQuery(self, query, cnx):
        cursor = cnx.cursor()
        try:
            cursor.execute(query)
        except mysql.connector.Error as error:
            print("Failed to select record from headline table {}".format(error))
            return None
        return cursor

    def getRecords(self, context, query):
        try:
            cnx = self.connect(context)
            cursor = self.getExecuteSelectQuery(query, cnx)
            records = cursor.fetchall()
            self.closeConnection(cnx)
        except mysql.connector.Error as error:
            print("Failed to get records from headline table {}".format(error))
        return records

    def insertRecord(self, context, sql):
        cnx = self.connect(context)
        try:
            cursor = cnx.cursor()
            cursor.execute(sql)
            self.closeConnection(cnx)
            return True
        except Exception as error:
            print("Failed to insert record into Laptop table {}".format(error))
        finally:
            if (cnx.is_connected()):
                cnx.close()
                return False;
