import os
import io
def tail(fname, n):
    buffer = io.DEFAULT_BUFFER_SIZE

    with open(fname) as f:
        if not f.seekable():
            from collections import dequeue
            dq = deque(f, n)
            
        fsize = os.stat(fname).st_size

        pos = 0
        itr = 0
        data = []
        while True:
            itr += 1
            f.seek(fsize - buffer*itr)
            pos=f.tell()
            data.extend(f.readlines())
            if len(data) >= n or pos == 0:
                return ''.join(data[-n:])

print(tail("install.log",10))

