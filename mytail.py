import sys
import os
import time
import io 
from pathlib import Path
import signal
from collections import deque
import functools

start_time = time.time()
@functools.lru_cache(maxsize=128)
def tail(fname, lines):
    def rendering(f, sep=''):
        if sep != '':
            data.extend('\n')
        data.extend(f.readlines())
        if len(data) >= lines or f.tell() == 0 or f.tell() == fsize:
            print(''.join(data[-lines:]))
            
    SLEEP_INTERVAL = 1.0
    bufsize = io.DEFAULT_BUFFER_SIZE
    fsize = os.stat(fname).st_size

    if fsize < 1:
        print("Invalid file")
        return

    iter = 0
    with open(fname) as f:
        if not f.seekable():
            from collections import deque
            dq = deque(f, lines)
            for l in dq:
                print(l)

        if bufsize > fsize:
            bufsize = fsize
        print("fsize {} bufsize {}".format(fsize, bufsize))
        data = []
        # for -n 
        while True:
            iter +=1
            
            f.seek(fsize-bufsize*iter)
            pos = f.tell()
            # rendering(f)
            data.extend(f.readlines())
            if len(data) >= lines or pos == 0:
                return ''.join(data[-lines:])
                
        # for -f
        # while True:
        #     signal.signal(signal.SIGINT, signal_handler)
        #     where = f.tell()
        #     line = f.readline()
        #     if not line:
        #         time.sleep(SLEEP_INTERVAL)
        #         f.seek(where)
        #     else:
        #         rendering(f, 1)

def signal_handler(sig, frame):
    sys.exit(0)

def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func

lines = int(sys.argv[2])
fname = sys.argv[1]
assert Path(fname).exists(), "file not exist"
print(tail(fname, lines))
end_time = time.time()

print("total time taken {}".format(end_time-start_time))