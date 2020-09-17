input_list = [1,3,4,5,6,1,3,2,5,1,1,4,4,2,2,4,6,7,4,2,6,2,2,6,7,8,8,5]
store = {}
for i in input_list:
    if i in store:
        store[i] += 1
    else:
        store[i] = 1
        
store = sorted(store.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
print(store[0][0])