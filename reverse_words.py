def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        n = len(words)
        result = ''
        for i in range(n-1,-1,-1):
            if words[i] != '':
                result += words[i].strip() + ' '
        
        return result.strip()