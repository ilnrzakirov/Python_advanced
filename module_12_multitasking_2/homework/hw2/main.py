import subprocess

import psutil


def process_count(username: str) -> int:
    proc_count = 0
    ps = subprocess.run(["ps", f"-U {username}"], capture_output=True)
    res = subprocess.run(["wc", "-l"], input=ps.stdout, capture_output=True)
    try:
        proc_count = int(res.stdout.decode("utf-8"))
    except Exception:
        print("Ошибка")
    return proc_count


def total_memory_usage(root_pid: int) -> float:
    # суммарное потребление памяти древа процессов
    # с корнем root_pid в процентах
    ps = psutil.Process(36970)
    children = ps.children()
    mem_size = ps.memory_info().rss
    for child in children:
        mem_size += psutil.Process(child.pid).memory_info().rss
    return mem_size


if __name__ == "__main__":
    print(process_count("ilnur"))
    print(total_memory_usage(36970))
