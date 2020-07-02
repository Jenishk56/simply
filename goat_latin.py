def toGoatLatin(self, S: str) -> str:
    vowel = set(["a","e","i","o","u", "A", "E", "I", "O", "U"])
    result = ""
    words = S.split(" ")
    word_counter = 0
    for word in words:
        start_char = word[0]
        if start_char not in vowel:
            word = word.replace(start_char, "", 1)
            word += start_char
        word += "ma"
            
        word += "a"*(word_counter+1)
        word_counter += 1
        result += word + " "
    
    return result.strip()