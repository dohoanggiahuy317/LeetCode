import random

class RandomizedSet:

    def __init__(self):
        self.d = set()

    def insert(self, val: int) -> bool:
        b = True
        if val in self.d:
            return False
        self.d.add(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.d:
            self.d.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        p = random.randint(0, len(self.d) - 1)
        return list(self.d)[p]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()