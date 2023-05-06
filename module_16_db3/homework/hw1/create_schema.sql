CREATE TABLE IF NOT EXISTS 'actors' (
    act_id INTEGER PRIMARY KEY AUTOINCREMENT,
    act_first_name VARCHAR(50) NOT NULL,
    act_last_name VARCHAR(50) NOT NULL,
    act_gender VARCHAR(1) NOT NULL
);

INSERT INTO "actors" (act_first_name, act_last_name, act_gender) VALUES
                    ("Петр", "Петров", "М"), ("Иван", "Иванов", "М");


CREATE TABLE IF NOT EXISTS 'movie' (
    mov_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mov_title VARCHAR(50) NOT NULL
);

INSERT INTO "movie" (mov_title) VALUES ("Фильм 1"), ("Фильм 2");

CREATE TABLE IF NOT EXISTS 'director' (
    dir_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dir_first_name VARCHAR(50) NOT NULL,
    dir_last_name VARCHAR(50) NOT NULL
);

INSERT INTO 'director' (dir_first_name, dir_last_name) VALUES
        ("Иван", "Козлов"), ("Павел", "Сидров");

