class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        t = s.lower()
        while i < j:
            if not t[i].isalnum(): i += 1
            elif not t[j].isalnum(): j -= 1
            else:
                if t[i] != t[j]: return False
                i += 1
                j -= 1
        return True
                
        
                