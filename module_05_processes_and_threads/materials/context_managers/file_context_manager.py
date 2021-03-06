import contextlib


class SavedFile:
    def __init__(self, path: str, exp_type: list, mode='r'):
        self.name = path
        self.mode = mode
        self.exp = exp_type

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        if type in self.exp:
            print("Exception {} has been handled".format(type))
            self.file.close()
            return True


if __name__ == '__main__':
    with SavedFile('some', [AttributeError, ValueError], 'w') as f:
        f.undefined('hello')
