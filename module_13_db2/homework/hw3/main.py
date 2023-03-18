import datetime
import sqlite3


def log_bird(
        cursor: sqlite3.Cursor,
        bird_name: str,
        date_time: str,
        count: int,
) -> None:
    query = f"""
        INSERT INTO table_bird (name, count, time)
        VALUES ('{bird_name}', {count} ,'{date_time}')
    """
    cursor.execute(query)


def check_if_such_bird_already_seen(
        cursor: sqlite3.Cursor,
        bird_name: str,
) -> bool:
    query = f"""
        SELECT COUNT(*) > 1 FROM table_bird
        WHERE  name = '{bird_name}'
    """
    cursor.execute(query)
    return cursor.fetchone()[0]



if __name__ == "__main__":
    print("Программа помощи ЮНатам v0.1")
    name: str = input("Пожалуйста введите имя птицы\n> ")
    count_str: str = input("Сколько птиц вы увидели?\n> ")
    count: int = int(count_str)
    right_now: str = datetime.datetime.utcnow().isoformat()

    with sqlite3.connect("../homework.db") as connection:
        cursor: sqlite3.Cursor = connection.cursor()
        cursor.execute(
            """CREATE TABLE  IF NOT EXISTS table_bird (
            name VARCHAR(500) NOT NULL,
            count INTEGER not null,
            time DATETIME not null
        );
        """,
        )
        log_bird(cursor, name, right_now, count)

        if check_if_such_bird_already_seen(cursor, name):
            print("Такую птицу мы уже наблюдали!")
