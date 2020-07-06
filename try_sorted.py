with open("fortune.txt") as f:
    from collections import deque
    dq = deque(f, 10)
    print(dq)
    for l in dq:
        print(l)