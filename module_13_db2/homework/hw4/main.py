import sqlite3
import pydantic


class Employer(pydantic.BaseModel):
    name: str
    salary: int

IVAN_SALARY_QUERY = """
        SELECT em.salary FROM table_effective_manager em
        WHERE em.name = "Иван Совин"
    """

with sqlite3.connect('../homework.db') as conn:
    cursor: sqlite3.Cursor = conn.cursor()
    IVAN_SALARY = cursor.execute(IVAN_SALARY_QUERY).fetchone()[0]


def get_employer(name: str) -> str:
    query = f"""
        SELECT * FROM table_effective_manager em
        WHERE name LIKE '{name}_%_%'
    """
    return query


def ivan_sovin_the_most_effective(
        cursor: sqlite3.Cursor,
        name: str,
) -> None:
    res = cursor.execute(get_employer(name))
    if data := res.fetchone():
        employer = Employer(
            name=data[1],
            salary=data[2]
        )
        if employer.name == "Иван Совин":
            return
        if employer.salary >= IVAN_SALARY:
            ...
        else:
            ...


if __name__ == '__main__':
    name: str = input('Введите имя сотрудника: ')
    with sqlite3.connect('../homework.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        ivan_sovin_the_most_effective(cursor, name)
        conn.commit()
