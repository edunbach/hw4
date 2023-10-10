#Q8 log.py with timestamp

import time

def timestamp(func):
    def wrapper(*args, **kwargs):
        current_time = time.ctime() #from hint in problem
        print(current_time)
        result = func(*args, **kwargs)
        return result
    return wrapper
