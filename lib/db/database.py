import sqlite3

class DBManager:

    def __init__(self, name):
        self.name = name

    def execute(self, query):
        db = sqlite3.connect(self.name)
        cursor = db.cursor()
        cursor.execute(query)
        lastid = cursor.lastrowid
        db.commit()
        db.close()
        return lastid

    def fetch(self, query):
        db = sqlite3.connect(self.name)
        cursor = db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        db.commit()
        db.close()
        return result

    def insert(self, table, bundles):
        keys = []
        values = []

        for key in bundles:
            keys.append(key)
            values.append(bundles[key])

        values = ["'{}'".format(x) for x in values]
        query = "insert into " + table + " ( "
        query += ", ".join(keys)
        query += ") values ( "
        query += ", ".join(values)
        query += ")"

        success = self.execute(query)

        return success

    def preview(self, table, fields=[]):

        if len(fields) > 0:
            fieldList = ','.join(fields)
        else:
            fieldList = '*'

        query = "select {} from {}".format(fieldList, table)
        return self.fetch(query)

    def createTable(self, title, fields):
        query = 'create table '
        query += title + " ( "
        count = 0
        for key in fields:
            if count > 0:
                query += ", "

            query += key + " " + fields[key]
            count += 1

        query += " )"

        test = self.execute(query)

    def dropTable(self, title):
        query = 'drop table ' + title
        self.execute(query)
