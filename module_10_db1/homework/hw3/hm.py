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
    cursor.execute("SELECT DISTINCT id FROM 'table_1'")
    unique_record_table_1 = cursor.fetchall()
    cursor.execute("SELECT COUNT(table_1.id) FROM 'table_1' JOIN table_2 t on table_1.id = t.id WHERE table_1.id == t.id")
    repetition_table_1_2 = cursor.fetchall()
    print(f"Длина таблицы 1{table_1_size}")
    print(f"Длина таблицы 2{table_3_size}")
    print(f"Длина таблицы 3{table_3_size}")
    print(f"Уникальных записей в таблице 1{len(unique_record_table_1)}")
    print(f"Повторений: {repetition_table_1_2}")


