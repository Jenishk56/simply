flat_list = []
def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    print(S)
    return S[:1] + flatten(S[1:])

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