def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfu = {}
        self.lru = {}
        self.cache = {}
        self.when = 1

    def get(self, key: int) -> int:
        
        if key in self.cache:
            if key in self.lfu:
                self.lfu[key] += 1
            else:
                self.lfu[key] = 1
            self.lru[key] = self.when
            self.when += 1
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            cache_len = len(self.cache)
            if key not in self.cache and cache_len >= self.capacity:
                old_keys = list()
                min_value = min(self.lfu.keys(), key=(lambda k: self.lfu[k]))
                for k, v in self.lfu.items():
                    if min_value == v:
                        old_keys.append(k)
                
                if len(old_keys) > 1:
                    when = float('inf')
                    for k in old_keys:
                        if self.lru[k] < when:
                            when = self.lru[k]
                            old_key = k
                else:
                    old_key = min(self.lfu, key=self.lfu.get)
                
                self.lfu.pop(old_key, None)
                self.cache.pop(old_key, None)
                # Got the space now, Bingo !    

            self.cache[key] = value
            if key in self.lfu:
                self.lfu[key] += 1
            else:
                self.lfu[key] = 1
            self.lru[key] = self.when
            self.when += 1