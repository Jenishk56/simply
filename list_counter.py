import time
start_time = time.time()
import collections
counter = {}
with open("fortune.txt") as f:
    for line in f:
        words = line.split(' ')
        for i in words:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
 
print(counter)
end_time = time.time()
print("Time taken {}".format(end_time-start_time))
