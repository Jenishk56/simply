import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        result = func(*args, **kwargs)
        print(f'Elapsed time is {time() - start} ms')
        return result
    return wrapper

@measure_time
def add(x, y):
    return x + y


add(2, 5)

def logger(func):
    from datetime import datetime
    def wrapper(*args, **kwargs):
        print('_' * 25)
        print(f'Run on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(func.__name__)
        func(*args, **kwargs)
        print('_' * 25)
    return wrapper

@logger
def shutdown():
    print('System shutdown')


@logger
def restart():
    print('System restarts')

shutdown()
restart()
