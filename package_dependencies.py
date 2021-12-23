def listOrder():
    permMarks = []
    tempMarks = []
    result = []
    processes = {}
    processes[0] = []
    processes[1] = [0]
    processes[2] = [0]
    processes[3] = [2]
    processes[4] = [5]
    processes[5] = [3]
    for process in processes:
        if process not in permMarks:
            visit(process, processes, tempMarks, permMarks, result)
    
    print(result)

def visit(process, processes, tempMarks, permMarks, result):
    if process in tempMarks:
        return
    if process not in permMarks:
        tempMarks.append(process)
        for values in processes[process]:
            visit(values, processes, tempMarks, permMarks, result)

        permMarks.append(process)
        tempMarks.remove(process)
        result.append(process)

listOrder()
