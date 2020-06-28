def makevalid(s: str) -> bool:
    stk = []
    bracket_map = {')':'(','}':'{',']':'['}
    s_list = list(s)
    count = 0
    indexer = []
    for char in s_list:
        if char in bracket_map:
            if stk:
                top = stk.pop()
                indexer.pop()
            else:
                top = '/'
            if bracket_map[char] != top:
                s_list[count] = ''
        else:
            if char in bracket_map.values():
                stk.append(char)
                indexer.append(count)
        count+=1
        
    if stk:
        n = len(stk)
        for i in range(n):
            s_list[indexer[i]] = ''
    return ''.join(s_list)

print(makevalid("b(d){{ss{}s}}}}}{{{{{a"))
