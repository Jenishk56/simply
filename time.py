def waitingTime(tickets, p):
    i, total_steps = 0, 0
    for num in tickets:
        if num < tickets[p]:
            total_steps += num
        else:
            if i > p:
                total_steps += tickets[p] - 1
            else:
                total_steps += tickets[p]
        i += 1
    return total_steps

print(waitingTime([1,2,5], 1))