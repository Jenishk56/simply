def testing():
    dic = {}
    dic[0] = 2
    dic[1] = 1
    dic[2] = 5
    dic[3] = 3

    dic = sorted(dic.items(), key = lambda kv:kv[1], reverse=True)
    print(dic)

testing()