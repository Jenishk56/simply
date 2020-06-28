import time
import sys

start_time = time.time()
import os
from functools import lru_cache

filename = "install.log"
moddate = os.path.getmtime(filename)
modmin = int((time.time()-moddate)/60)

# @lru_cache(maxsize=32)
def taily(file, n):
    count = 0
    textfile = open(file)
    lines = textfile.readlines()
    result_lines = []
    for line in reversed(lines):
        if count >= 10:
            break
        result_lines.append(line.rstrip())
        count+=1

    print('\n'.join(result_lines[::-1]))
        


# if modmin < 10:
    # taily.cache_clear()

taily(sys.argv[1], sys.argv[2])
end_time = time.time()
print("total time taken {}".format(end_time-start_time))