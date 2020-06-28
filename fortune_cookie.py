import random
import os, time
moddate = os.path.getmtime("install.log")
modmin = int((time.time()-moddate)/60)
start_time = time.time()
print("start time {}".format(start_time))

def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func
    
from functools import lru_cache
@lru_cache(maxsize=32)
def randomfortune():
    with open("install.log") as f:
        lines=f.readlines()

    return lines

if modmin < 10:
    randomfortune.cache_clear()
    print("with clear cache time {}".format(time.time()))
else:
    print("without clear cache time {}".format(time.time()))

lines = randomfortune()
print(random.choice(lines))

end_time = time.time()
print("end time {}".format(end_time))
print("difference start to end {}".format(end_time-start_time))