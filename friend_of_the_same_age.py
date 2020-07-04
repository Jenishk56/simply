import collections
def numFriendRequests(self, ages) -> int:
    def request(a, b):
        return not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100)
    
    count = 0
    c = collections.Counter(ages)
    for a in c:
        for b in c:
            # Reusing the duplicates, removing the same element
            self_remove = 0
            if a == b:
                self_remove = 1
                
            count += request(a, b) * c[a] * (c[b] - self_remove)
    
    return count