import sqlite3
from sqlite3 import Error


def init_analytics_table():
    try:
        con = sqlite3.connect('blog_framework.db')
        cur = con.cursor()
        sql_drop_table_analytics = """ DROP TABLE IF EXISTS analytics;
            """
        sql_create_table_analytics = """CREATE TABLE IF NOT EXISTS analytics (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    route TEXT NOT NULL,
                                    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                                );"""

        cur.execute(sql_drop_table_analytics)
        con.commit()
        print(sql_create_table_analytics)
        cur.execute(sql_create_table_analytics)
        print(cur.fetchall())
        con.commit()
        con.close()
    except Error as e:
        print(e)


if __name__ == '__main__':
    init_analytics_table()
