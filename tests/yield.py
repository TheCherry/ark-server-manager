import time


class controlled_execution:
    def __enter__(self):
        for i in range(1, 5):
            return i

    def __exit__(self, type, value, traceback):
        t = ""

with controlled_execution() as thing:
    print(thing)
