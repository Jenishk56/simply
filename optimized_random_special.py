import random
import time
import os
def findrandom():
    def randomfinder(fsize):
        bufsize = random.randrange(fsize-1)
        f.seek(bufsize)
        f.readline()
        return f

    with open("random_big.txt") as f:
        result = ''
        prev = ''
        fsize = os.stat("random_big.txt").st_size
        f = randomfinder(fsize)
        for line in f:
            line = line.strip()
            if line == '':
                while line == '':
                    f = randomfinder(fsize)
            if line == "%" and prev != line:
                break
            else:
                if result == '':
                    result = line
                else:
                    result = result + "\n" + line
            prev = line
    
    return result

start_time = time.time()
print(findrandom())
print("Total time taken {}".format(time.time() - start_time))