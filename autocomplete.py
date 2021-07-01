class LinearSearch:
    def __init__(self):
        self.data = []
        
    def index(self, suggestions):
        for i in suggestions:
            self.data.append(i)
        self.data.sort()

    def search(self, pre):
        start_position = 0
        counter = 0
        for value in self.data:
            if pre[0] == value[0]:
                start_position = counter
                break
            counter += 1

        for i in self.data[start_position:]:
            if i.startswith(pre):
                yield i
            else:
                break
        

search1 = LinearSearch()
search1.index(["adasdsad","asdsadAD","sadas","hi", "hello", "how are", "nanan"])
for value in search1.search("h"):
    print(value)