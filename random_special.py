import random
import time

def findrandom():
    with open("random_big.txt") as f:
        dic = {}
        line_count = 0
        prev = ''
        for line in f:
            line = line.strip()
            if line == "%":
                if prev != line:
                    line_count += 1
            else:
                if line_count not in dic:
                    dic[line_count] = line
                else:
                    dic[line_count] = dic[line_count] + "\n" + line
            prev = line
    
    return random.choice(dic)

start_time = time.time()
print(findrandom())
print("Total time taken {}".format(time.time() - start_time))