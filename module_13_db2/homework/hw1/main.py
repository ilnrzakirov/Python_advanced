import sqlite3


def check_if_vaccine_has_spoiled(
        cursor: sqlite3.Cursor,
        truck_number: str,
) -> bool:
    query = f"""
    SELECT COUNT(*) > 3 FROM table_truck_with_vaccine tb
        WHERE tb.truck_number = '{truck_number}' AND tb.temperature_in_celsius NOT BETWEEN 16 AND 20
    """
    cursor.execute(query)
    return cursor.fetchone()[0]


if __name__ == "__main__":
    truck_number: str = input("Введите номер грузовика: ")
    with sqlite3.connect("../homework.db") as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        spoiled: bool = check_if_vaccine_has_spoiled(cursor, truck_number)
        print("Испортилась" if spoiled else "Не испортилась")
        conn.commit()
