from datetime import datetime
import time
def timemachine(file_name):
    def decor_time(func):
        before = datetime.now()
        print(before)
        func()
        after = datetime.now()
        print(after)
        result = after - before
        print(f"this function running time was: {result.seconds}")
        with open(file_name, "w") as file:
            print(f"{datetime.now()} | function {str(func).split()[1]} have run {result.seconds} seconds.", file=file)    
    return decor_time


@timemachine("timelog.log")
def sleep_func():
    time.sleep(5)




