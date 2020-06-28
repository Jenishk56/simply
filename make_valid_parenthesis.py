def makevalid(s: str) -> bool:
    stk = []
    bracket_map = {')':'(','}':'{',']':'['}
    s_list = list(s)
    count = 0
    for char in s_list:
        if char in bracket_map:
            top = stk.pop() if stk else '/'
            if bracket_map[char] != top:
                s_list[count] = ''
        else:
            if char in bracket_map.values():
                stk.append(char)
        count+=1
    return ''.join(s_list)

print(makevalid("b(d)ss{}s}a"))
