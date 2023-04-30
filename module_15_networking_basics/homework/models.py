import sqlite3
from typing import Optional, Any


class Room:
    def __init__(self, id: Optional[int], floor: int, beds: int, guestNum: int, price: int):
        self.id: int = id
        self.floor: int = floor
        self.beds: int = beds
        self.guestNum: int = guestNum
        self.price: int = price

    def __getitem__(self, item: str) -> Any:
        return getattr(self, item)

def init_db() -> None:
    with sqlite3.connect('table_room.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS `table_rooms` (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    floor INTEGER, 
                    beds INTEGER,
                    guestNum INTEGER,
                    price INTEGER
                );
            """
        )


def add_room_to_db(room: Room):
    with sqlite3.connect('table_room.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        query = f"""
                  INSERT INTO table_rooms (floor, beds, guestNum, price) VALUES 
                  (?, ?, ?, ?)
                      """
        cursor.execute(query, (room.floor, room.beds, room.guestNum, room.price))


def get_rooms(checkIn: str = None, checkOut: str = None) -> list[Room]:
    with sqlite3.connect('table_room.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        if checkIn and checkOut:
            cursor.execute(
                """
                    SELECT * from `table_rooms`
                """
            )
        else:
            cursor.execute(
                """
                SELECT * from `table_rooms`
                """
            )
        return [Room(*row) for row in cursor.fetchall()]
