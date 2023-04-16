import copy
import datetime
import random
import sqlite3

import pydantic


class Employer(pydantic.BaseModel):
    id: int
    name: str
    preferable_sport: str


SPORT_DAY_DICT = {
    0: "футбол",
    1: "хоккей",
    2: "шахматы",
    3: "SUP сёрфинг",
    4: "бокс",
    5: "Dota2",
    6: "шах-бокс"
}


def get_employees(cursor: sqlite3.Cursor) -> list[Employer]:
    employees_list: list[Employer] = []
    query = """
        SELECT * FROM table_friendship_employees 
    """
    cursor.execute(query)
    res = cursor.fetchall()
    for employer in res:
        employees_list.append(Employer(
            id=employer[0],
            name=employer[1],
            preferable_sport=employer[2]
        ))
    return employees_list


def to_dict(employees: list[Employer]) -> dict:
    sport_dict: dict = {}
    for employer in employees:
        if employer.preferable_sport in sport_dict:
            sport_dict[employer.preferable_sport].append(employer)
        else:
            sport_dict[employer.preferable_sport] = [employer]
    return sport_dict


def get_sport_without_weekday(weekday_sport: str) -> str:
    num = random.randint(0, 6)
    sport = SPORT_DAY_DICT[num]
    while weekday_sport == sport:
        num = random.randint(0, 6)
        sport = SPORT_DAY_DICT[num]
    return sport


def update_work_schedule(cursor: sqlite3.Cursor) -> None:
    employees = get_employees(cursor)
    rm = to_dict(employees)
    employees_dict_for_sport = copy.deepcopy(rm)
    schedule_parameters: list[dict] = []
    for day in range(1, 366):
        date = datetime.datetime(year=2020, day=1, month=1) + datetime.timedelta(days=day)
        weekday = date.weekday()
        weekday_sport = SPORT_DAY_DICT[weekday]
        for employer_num in range(10):
            sport = get_sport_without_weekday(weekday_sport)
            while not employees_dict_for_sport[sport]:
                sport = get_sport_without_weekday(weekday_sport)
                if not employees_dict_for_sport[sport]:
                    employees_dict_for_sport = copy.deepcopy(rm)
            employer = employees_dict_for_sport[sport].pop(0)
            schedule_parameters.append({
                "employee_id": employer.id,
                "date": date
            })
    query = f"""
        INSERT INTO table_friendship_schedule (employee_id, date) VALUES (
            :employee_id,
            :date
        )
    """
    cursor.executemany(query, schedule_parameters)




if __name__ == '__main__':
    with sqlite3.connect('../homework.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        delete_query = "DELETE FROM table_friendship_schedule"
        cursor.execute(delete_query)
        update_work_schedule(cursor)
        conn.commit()
