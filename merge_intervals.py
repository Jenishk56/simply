class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        m = [] 
        s = -10000
        max = -100000
        for i in range(len(intervals)): 
            a = intervals[i] 
            if a[0] > max: 
                if i != 0: 
                    m.append([s,max]) 
                max = a[1] 
                s = a[0] 
            elif a[1] >= max: 
                max = a[1]
        
        if s != -10000 and max != -10000:
            m.append([s,max])
                    
        return m