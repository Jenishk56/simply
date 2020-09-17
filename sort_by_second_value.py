def sort(dataFile):
    result = {}
    # with open(dataFile) as r:
    data = dataFile.split("\n")
    count = 0
    data_len = len(data)
    for lines in data:
        if count == 0 or count == data_len-1:
            count+=1
            continue
        entries = lines.split(",")
        sorting_value = entries[1]
        if sorting_value not in result:
            result[sorting_value] = [[entries[0],entries[1],entries[2]]]
        else:
            result[sorting_value].append([entries[0],entries[1],entries[2]])
        count+=1
                
    sorted(result)
    for value in result.values():
        for ele in value:
            print(",".join(ele))
   
dataFile="""
"entry1",2,3.6
"boots",5,1.7
"slack",1,2.6
"triffid",11,-1.5
"""
sort(dataFile)

