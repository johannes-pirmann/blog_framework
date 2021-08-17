import sqlite3
from sqlite3 import Error


class DatabaseHandler:
    def __init__(self, path_to_db):
        self.database_path = path_to_db

    def execute_insert_query(self, sql_query, values):
        con = sqlite3.connect(self.database_path)
        cur = con.cursor()
        cur.execute(sql_query, values)
        con.commit()
        con.close()

    def execute_read_query(self, sql_query):
        con = sqlite3.connect(self.database_path)
        cur = con.cursor()
        cur.execute(sql_query)
        result = cur.fetchall()
        con.commit()
        con.close()
        return result
