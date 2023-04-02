import enum
import random
import sqlite3
import pycountry
import pydantic

COUNTRY_LIST = list(pycountry.countries)


class Command(pydantic.BaseModel):
    id: int
    name: str
    country: str
    level: str


class Group(pydantic.BaseModel):
    id: int
    commands: list[Command]


class Level(enum.IntEnum):
    WEAK = 1
    MEDIUM = 2 | 3
    STRONG = 4


def get_group(group_number: int) -> Group:
    levels: list[Level] = [Level.WEAK, Level.STRONG, Level.MEDIUM, Level.MEDIUM]
    return Group(
        id=group_number,
        commands=[Command(
            id=number + (group_number * 4),
            name="Command" + str(number),
            country=random.choice(COUNTRY_LIST).name,
            level=levels[number - 1].name
        ) for number in range(1, 5)]
    )


def set_groups(number_of_commands: int) -> list[Group]:
    group_list: list[Group] = []
    for group_number in range(1, number_of_commands + 1):
        group_list.append(
            get_group(group_number)
        )
    return group_list


def generate_test_data(
        cursor: sqlite3.Cursor,
        number_of_groups: int,
) -> None:
    groups = set_groups(number_of_groups)
    uefa_commands_parameters: list[dict] = []
    uefa_draw_parameters: list[dict] = []
    for group in groups:
        for command in group.commands:
            uefa_commands_parameters.append({
                "command_name": command.name,
                "command_country": command.country,
                "command_level": command.level
            })
            uefa_draw_parameters.append({
                "command_number": command.id,
                "group_number": group.id
            })
    commands_query = """
        INSERT INTO uefa_commands (command_name, command_country, command_level)
            VALUES (
                    :command_name, 
                    :command_country, 
                    :command_level
                    ) 
    """
    group_query = """
        INSERT INTO uefa_draw (command_number, group_number)
            VALUES (:command_number,
                    :group_number)
    """
    cursor.executemany(commands_query, uefa_commands_parameters)
    cursor.executemany(group_query, uefa_draw_parameters)


if __name__ == '__main__':
    number_of_groups: int = int(input('Введите количество групп (от 4 до 16): '))
    with sqlite3.connect('../homework.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        generate_test_data(cursor, number_of_groups)
        conn.commit()
