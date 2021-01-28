from datetime import datetime
import time
def timemachine(func):
    def decor_time():
        before = datetime.now()
        print(before)
        func()
        after = datetime.now()
        print(after)
        result = after - before
        print(f"this function running time was: {result.seconds}")
    return decor_time

@timemachine
def sleep_func():
    time.sleep(5)


sleep_func()

