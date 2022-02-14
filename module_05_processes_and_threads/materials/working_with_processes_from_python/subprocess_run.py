import subprocess


def run_program():
    res = subprocess.run(['python', 'test_program.py'], input=f'some input\ninput line 1\n'
                                                              f'input line 2\n input line 3', encoding='utf-8')
    print(res)


if __name__ == '__main__':
    run_program()
