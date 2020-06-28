
import os
import random
import time

start_time = time.time()
def fortune(fname):
    fsize = os.stat(fname).st_size
    with open(fname) as f:
        def randomfinder():
            bufsize = random.randrange(fsize-1)
            f.seek(bufsize)
            f.readline()

        randomfinder()
        result_line = f.readline()
        if result_line == '':
            while result_line == '':
                randomfinder()
                result_line = f.readline()
            
        print(result_line)

fortune("install.log")
end_time = time.time()
print("Total time taken {}".format(end_time-start_time))