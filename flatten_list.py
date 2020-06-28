flat_list = []
def flatten(input):
    for i, _ in enumerate(input):
        while i < len(input) and type(input[i]) == list:
            input[i:i+1] = input[i]
    return sum([list(x) for x in input], [])

# def explorelists(l):
#     result = []
#     for value in l:
#         result.append(value)
#     return result

# def juststore(thislist):
#     flat_list.append(thislist)

# def flatten(dothis):
#     flat_list.extend(dothis)
print(flatten(['aaa', 'bb', ['cccccc', 'xx', 'yyyyyyy'], [['ss', 'tt']]]))