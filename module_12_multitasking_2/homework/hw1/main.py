import datetime
import sqlite3


def download_form_pool():
    start_time = datetime.datetime.now()



def download_form_thread_pool():
    pass


def main():
    download_form_pool_time = download_form_pool()
    print(f"Pool: {download_form_pool_time}")
    download_form_thread_pool_time = download_form_thread_pool()
    print(f"ThreadPool: {download_form_thread_pool_time}")


if __name__ == "__main__":
    with sqlite3.connect("hw") as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS people;")
        cursor.execute("""CREATE TABLE people (
            name VARCHAR(500) NOT NULL,
            height INTEGER not null,
            mass INTEGER not null,
            gender VARCHAR(500) not null
        );""")
        conn.commit()
    main()