from handlers import database
"""
This script serves solely the purpose of testing the analytics and showing the results.
For future use is should be refactored!
"""

db = database.DatabaseHandler('blog_framework.db')
sql_distinct = "SELECT DISTINCT route FROM analytics;"
distinct_values = db.execute_read_query(sql_distinct)

for key in distinct_values:
    sql_count_distinct = "SELECT COUNT(*) FROM analytics WHERE route='" + key[0] + "';"
    count_of_key = db.execute_read_query(sql_count_distinct)
    print(key[0] + ': ' + str(count_of_key[0][0]))
