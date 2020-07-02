def isAlienSorted(self, words: List[str], order: str) -> bool:
    lookup = {}
    count = 0
    for char in order:
        lookup[char] = count + 1
        count+=1
    
    n = len(words)
    for i in range(n-1):
        word1 = words[i]
        word2 = words[i+1]
        n1 = len(word1)
        n2 = len(word2)
        n = min(n1, n2)
        count = 0
        for k in range(n):
            if word1[k] == word2[k]:
                count+=1
            else:
                if lookup[word1[k]] > lookup[word2[k]]:
                    return 0
                break
                
        if count == n and n1 > n2:
            return 0
                
    return 1