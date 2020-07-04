class buffer():
    def __init__(self, k):
        self.k = k
        self.buffer = [''] * k
        self.read = 0
        self.write = 0
        self.size = 0

    def put(self, str):
        n = len(str)
        i = 0
        
        # loop over the string and checking for the buffer full
        while i < n and (self.write != self.read or self.size != self.k):
            self.buffer[self.write] = str[i]
            self.write = (self.write + 1) % self.k
            self.size += 1
            i += 1
        
        return i

    def get(self, n):
        i, ret = 0, ''
        while i < n and (self.write != self.read or self.size != 0):
            ret += self.buffer[self.read]
            self.buffer[self.read] = ''
            self.read = (self.read + 1) % self.k
            self.size -= 1
            i += 1

        return ret

buf = buffer(5)
buf.put('xyz')
print(buf.get(3))
buf.put('abc')
buf.put('po')
print(buf.get(5))
        