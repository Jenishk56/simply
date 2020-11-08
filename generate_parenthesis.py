class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        def backtrack(current_string, open_p, close_p, max_l):
            if len(current_string) == max_l * 2:
                self.result.append(current_string)
                 
            if open_p < max_l:
                backtrack(current_string + "(", open_p+1, close_p, max_l)
            if close_p < open_p:
                backtrack(current_string + ")", open_p, close_p+1, max_l)
            
        
        backtrack("", 0, 0, n)
        return self.result