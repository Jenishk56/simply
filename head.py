from collections import deque
import time
import os
import io

start_time = time.time()
def head(n):
    fname = "install.log"
    fsize = os.stat(fname).st_size
    bufferSize = io.DEFAULT_BUFFER_SIZE
    data = []
    with open(fname) as f:
        pos = 0
        if bufferSize > fsize:
            bufferSize = fsize
        while pos <= fsize:
            next_slot = pos + bufferSize
            while f.tell() < next_slot and f.tell() <= fsize:
                line = f.readline(next_slot-f.tell())
                line = line.strip()
                data.append(line)
            if len(data) >= n:
                break
            pos += bufferSize

    return data[:n]

print(head(10))
print("Time difference {}".format(time.time()-start_time))

