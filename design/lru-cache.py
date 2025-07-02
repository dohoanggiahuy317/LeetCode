class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = {} # The actual cache to store key-val
        self.key_order = {} # tracking the order of the key is use, keep adding new key use here
        self.key_freq = defaultdict(int) # we gonna remove key with smallest order 
        self.count = 0
        self.curr_min = 0
        pass

    def get(self, key: int) -> int:
        
        if key in self.dict:
            self.key_order[self.count] = key
            self.key_freq[key] += 1
            self.count += 1
            return self.dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.key_freq[key] += 1
        self.key_order[self.count] = key
        self.count += 1
        self.dict[key] = value

        while len(self.key_freq) > self.cap:
            least_key = self.key_order[self.curr_min]
            self.key_freq[least_key] -= 1

            if self.key_freq[least_key] == 0:
                del self.key_freq[least_key]
                del self.dict[least_key]

            self.curr_min += 1
        
        # print(self.dict, self.key_order, self.key_freq)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)