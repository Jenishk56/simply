import traceback
from typing import Iterator

import os
import io
from time import sleep
from pathlib import Path
import time

class Solution:
    def __init__(self, file_path: str, chunksize: int=io.DEFAULT_BUFFER_SIZE, check_interval: float=0.1):
        self.file_path = file_path
        self.chunksize = chunksize
        self.check_interval = check_interval

        assert Path(file_path).exists(), f"{file_path} not exist"
        assert self.chunksize > 0 and self.check_interval > 0

    def tail(self, n: int = 10, follow: bool=True):
        assert n >= 0, "Only support postive inputs"
        print("hello")
        with open(self.file_path) as reader:
            if not reader.seekable():
                from collections import deque
                yield from deque(reader, n)
            else:
                # 1. seek to end
                cur = reader.seek(0, os.SEEK_END)

                # # 2. rewind cur_pos back n lines back
                # def rewind_n_lines(cur_pos: int, n: int) -> int:
                #     remaining = cur_pos

                #     while remaining > 0:
                #         cur_pos -= self.chunksize

                #         if cur_pos < 0:
                #             cur_pos = 0

                #         reader.seek(cur_pos)
                #         chunk = reader.read(self.chunksize)
                #         remaining -= len(chunk)

                #         n -= chunk.count(os.linesep)
                        
                #         if n <= 0 or 0 == remaining:
                #             break

                #     reader.seek(cur_pos)
                #     while n <= 0:
                #         # skip lines reversed more than n
                #         reader.readline()
                #         n += 1
                    
                #     return reader.tell()

                # reader.seek(rewind_n_lines(cur, n))

                # print("herllo")
                # print(reader.tell())
                # # 3. read lines
                # # while True:
                # line = reader.readlines()
                # for l in line:
                #     return l

if __name__ == '__main__':
    start_time = time.time()
    s = Solution("fortune.txt", chunksize=3)
    s.tail()
    # for line in s.tail():
    #     print(line, end="")
    end_time = time.time()
    print("Total time taken {}".format(end_time-start_time))