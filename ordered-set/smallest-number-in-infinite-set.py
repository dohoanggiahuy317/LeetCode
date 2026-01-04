class SmallestInfiniteSet:
            
    li = []

    def __init__(self):
        self.li = []
        i = 1
        while i < 1001:
            self.li.append(i)
            i+=1
        

    def popSmallest(self) -> int:
        if (len(self.li) > 0) :
            min_val = min(self.li)
            self.li.remove(min_val)

            return (min_val)


    def addBack(self, num: int) -> None:
        if num not in self.li:
            self.li.append(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)