class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        bracket_map = {')':'(','}':'{',']':'['}
        for char in s:
            if char in bracket_map:
                top = stk.pop() if stk else '/'
                if bracket_map[char] != top:
                    return 0
            else:
                stk.append(char)
        return not stk