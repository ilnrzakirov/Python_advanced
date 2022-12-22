import sqlite3

with sqlite3.connect("hw_3_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM 'table_1'")
    result = cursor.fetchall()
    print(result)


