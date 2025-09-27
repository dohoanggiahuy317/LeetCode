class NumberContainers:

    def __init__(self):
        self.num2idx = {}
        self.idx2num = {}

    def change(self, index: int, number: int) -> None:
        
        # Handle idx2num
        if index in self.idx2num:
            prev_num = self.idx2num[index]
            self.num2idx[prev_num].remove(index)

        self.idx2num[index] = number

        # handle num2idx
        if number not in self.num2idx:
            self.num2idx[number] = SortedSet()

        self.num2idx[number].add(index)
        

    def find(self, number: int) -> int:
        if number not in self.num2idx or len(self.num2idx[number]) == 0:
            return -1
        return self.num2idx[number][0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)