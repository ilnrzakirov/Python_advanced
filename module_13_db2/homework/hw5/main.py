import sqlite3
import pycountry
import pydantic

COUNTRY_LIST = list(pycountry.countries)


class Commands(pydantic.BaseModel):
    id: int
    name: str
    country: str
    level: int


class Group(pydantic.BaseModel):
    id: int
    commands: list[Commands]


def generate_test_data(
        cursor: sqlite3.Cursor,
        number_of_groups: int,
) -> None:
    ...


if __name__ == '__main__':
    number_of_groups: int = int(input('Введите количество групп (от 4 до 16): '))
    with sqlite3.connect('../homework.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        generate_test_data(cursor, number_of_groups)
        conn.commit()
