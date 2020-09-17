import os
import io
def tail(fname, n):
    buffer = io.DEFAULT_BUFFER_SIZE

    with open(fname) as f:
        fsize = os.stat(fname).st_size

        pos = 0
        itr = 0
        while True:
            itr += 1
            f.seek(fsize - buffer*itr)
            pos=f.tell()
            data.extend(f.readlines())
            if 

