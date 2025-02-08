class NumberContainers:

    def __init__(self):
        self.ind2val = {}
        self.val2ind = {}
        self.max = 0

    def change(self, index: int, number: int) -> None:
        if index in self.ind2val:
            val = self.ind2val[index]
            self.val2ind[val].remove(index)

        if number not in self.val2ind:
            self.val2ind[number] = set()
        self.val2ind[number].add(index)
        self.ind2val[index] = number

    def find(self, number: int) -> int:
        if number in self.val2ind and len(self.val2ind[number]) > 0:
            return min(self.val2ind[number])
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)