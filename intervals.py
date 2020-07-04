def leastInterval(tasks, n: int) -> int:
    count = {}
    for t in tasks:
        if t in count:
            count[t] += 1
        else:
            count[t]=1
    
    count = sorted(count.values(), reverse=True)
    max_num = max(count)
    
    max_task_num = 0
    for value in count:
        if value == max_num:
            max_task_num += 1
            
    return max(len(tasks), (max_num - 1) * (n + 1) + max_task_num)