max=int(input("How many prime numbers do you want: "))
min=2
while(min<=(max)):
    for c in range(2, min):
        if min%c==0:
            break
    else:
        print(min)
    min = min + 1