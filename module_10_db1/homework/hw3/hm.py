import sqlite3

with sqlite3.connect("hw_3_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM 'table_1'")
    result = cursor.fetchall()
    cursor.execute("SELECT * FROM 'table_2'")
    result_2 = cursor.fetchall()
    cursor.execute("SELECT * FROM 'table_3'")
    result_3 = cursor.fetchall()
    table_1_size = len(result)
    table_2_size = len(result_2)
    table_3_size = len(result_3)
    print(table_1_size)
    print(table_2_size)
    print(table_3_size)


