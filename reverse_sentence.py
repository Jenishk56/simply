import time
def reverseWords(s: str) -> str:
    n = len(s)
    result = ''
    for i in range(n-1,-1,-1):
        # if s[i] != '':
        result += s[i].strip()
    
    return result.strip()

start_time = time.time()
print(reverseWords("mynameisjenish"))
print("Time difference {}".format(time.time()-start_time))

start_time = time.time()
print("mynameisjenish"[::-1])
print("Time difference lib {}".format(time.time()-start_time))


start_time = time.time()
print(''.join(reversed('mynameisjenish')))
print("Time difference lib1 {}".format(time.time()-start_time))
