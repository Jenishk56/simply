import time
start_time = time.time()
import collections
counter = {}
with open("fortune.txt") as f:
    dq = collections.deque(f)
    for i in dq:
        counter[i] = dq.count(i)

print(counter)
end_time = time.time()
print("Time taken {}".format(end_time-start_time))
