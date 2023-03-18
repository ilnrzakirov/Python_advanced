import csv
import sqlite3


def delete_wrong_fees(
        cursor: sqlite3.Cursor,
        wrong_fees_file: str,
) -> None:
    param: list[dict] = []
    with open(wrong_fees_file, newline="\n") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader)
        for line in reader:
            param.append(
                {"time": line[1], "number": line[0]},
            )
    query = """
        DELETE FROM table_fees
        WHERE (timestamp= :time AND truck_number= :number)
    """
    cursor.executemany(query, param)


if __name__ == "__main__":
    with sqlite3.connect("../homework.db") as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        delete_wrong_fees(cursor, "../wrong_fees.csv")
        conn.commit()
