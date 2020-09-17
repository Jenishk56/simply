d = {'A': 10, 'B':5, 'C':5, 'D':12, 'E':3}
d2 = {}

for key, value in d.items():
    if value not in d2:
        d2[value] = key
    else:
        d2[value] = d2[value] + ", " + key

for key, value in d2.items():
    print("{}: {}".format(key, value))