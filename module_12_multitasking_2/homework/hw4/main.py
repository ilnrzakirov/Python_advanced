import datetime
import queue
import threading
import time

import requests

URL = "http://127.0.0.1:8080/timestamp/"


def write_log(q: queue.Queue):
    if job := q.get():
        timestamp_datetime = datetime.datetime.strptime(job[1], "%Y-%m-%d %H:%M:%S.%f")
        with open("log.log", "a") as file:
            file.write(f"{datetime.datetime.isoformat(timestamp_datetime)}\n")


def worker(q: queue.PriorityQueue):
    start_time = datetime.datetime.now()
    while datetime.datetime.now() < start_time + datetime.timedelta(seconds=20):
        try:
            response = requests.get(f"{URL}{datetime.datetime.now().timestamp()}")
            resp_time = response.text
            priority = int(resp_time.split(".")[1])
            q.put((priority, resp_time))
            write_log(q)
            time.sleep(1)
        except requests.exceptions.RequestException as e:
            print(f"error: {e}")


def main():
    try:
        q = queue.PriorityQueue(10)
        tasks: list[threading.Thread] = []
        for _ in range(10):
            thread_worker = threading.Thread(target=worker, daemon=True, args=[q])
            tasks.append(thread_worker)
            thread_worker.start()
            time.sleep(1)

        for task in tasks:
            task.join()
    except KeyboardInterrupt:
        exit(1)


if __name__ == "__main__":
    main()
