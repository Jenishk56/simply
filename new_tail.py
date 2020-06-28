import os
import io
import time
def taily(n: int = 10, follow: bool=True):
    chunksize=io.DEFAULT_BUFFER_SIZE
    with open("install.log") as reader:
        cur = reader.seek(0, os.SEEK_END)
        # # 2. rewind cur_pos back n lines back
        def rewind_n_lines(cur_pos: int, n: int) -> int:
            remaining = cur_pos

            while remaining > 0:
                cur_pos -= chunksize

                if cur_pos < 0:
                    cur_pos = 0

                reader.seek(cur_pos)
                chunk = reader.read(chunksize)
                remaining -= len(chunk)

                n -= chunk.count(os.linesep)
                
                if n <= 0 or 0 == remaining:
                    break

            reader.seek(cur_pos)
            while n <= 0:
                # skip lines reversed more than n
                reader.readline()
                n += 1
            
            return reader.tell()

        reader.seek(rewind_n_lines(cur, n))

        # 3. read lines
        # while True:
        line = reader.readlines()
        for l in line:
            print(l)

start_time = time.time()
taily()
end_time = time.time()
print("Time it took {}".format(end_time-start_time))