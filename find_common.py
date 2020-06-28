import time
start_time = time.time()
list1 = [1,2,3,4,5,6]
list2 = [3, 5, 7, 9]
set_list1, set_list2 = set(list1), set(list2)
result = set()
for i in set_list1:
    if i in set_list2:
        result.add(i)

print(result)
# print(list(set(list1).intersection(list2)))
end_time = time.time()

print("Time Difference {}".format(end_time-start_time))