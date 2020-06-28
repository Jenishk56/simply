def test():
    with open("fortune.txt") as f:
        from collections import deque
        dq = deque(f, 10)
        for l in dq:
            print(l)

test()