import os
import io
def tail(fname, n):
    buffer = io.DEFAULT_BUFFER_SIZE
    fsize = os.stat(fname).st_size

    pos = 0
    while 
