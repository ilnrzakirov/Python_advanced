import sqlite3

with sqlite3.connect("hw_4_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(id) FROM salaries WHERE salary < 5000")
    result = cursor.fetchone()
    print(result)
    cursor.execute("SELECT AVG(salary) FROM salaries")
    avg_salary = cursor.fetchone()
    print(avg_salary)
    cursor.execute("SELECT salary FROM salaries ORDER BY salary LIMIT 1 OFFSET (SELECT COUNT(*) FROM salaries) / 2")
    median = cursor.fetchone()
    print(median)