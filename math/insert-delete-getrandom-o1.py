class RandomizedSet:

    def __init__(self):
        self.val2idx = {}
        self.li = []

    def insert(self, val: int) -> bool:
        if val in self.val2idx:
            return False
        self.val2idx[val] = len(self.li)
        self.li.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val2idx:
            return False
        
        idx = self.val2idx[val]
        last_val = self.vals[-1]
        
        self.vals[idx], self.val2idx[last_val] = last_val, idx
        
        self.vals.pop()
        del self.val2idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()