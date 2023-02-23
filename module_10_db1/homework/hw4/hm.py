import sqlite3

with sqlite3.connect("hw_4_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM salaries WHERE salary < 5000")
    result = cursor.fetchone()
    print(result)
    cursor.execute("SELECT AVG(salary) FROM salaries")
    avg_salary = cursor.fetchone()
    print(avg_salary)
    cursor.execute("SELECT salary FROM salaries ORDER BY salary LIMIT 1 OFFSET (SELECT COUNT(*) FROM salaries) / 2")
    median = cursor.fetchone()
    print(median)
    cursor.execute(
        f"""
            SELECT 
                100 * ROUND(
                (
                    SELECT SUM(salary) FROM salaries ORDER BY salary DESC LIMIT 0.1 * (
                    SELECT COUNT(*) FROM salaries)
                ) / (
                    SELECT SUM(salary) FROM salaries ORDER BY salary ASC LIMIT 0.9 * (
                    SELECT COUNT(*) FROM salaries))
                , 2)
            FROM salaries
        """
    )
    res = cursor.fetchone()
    print(res)


def find_position(x: int, a: list[int]) -> int:
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1


def find_insert_position(x: int, a: list[int]) -> int:
    len_a = len(a)
    if len_a == 0 or a[0] > x:
        return 0
    elif a[len_a - 1] < x:
        return len_a
    pos = find_position(x, a)
    return pos

print(find_insert_position(5, [0, 1, 3, 5, 7, 9]))

