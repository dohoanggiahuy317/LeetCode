class NumberContainers:

    def __init__(self):
        self.d = {}
        self.max = 0

    def change(self, index: int, number: int) -> None:
        self.d[index] = number
        self.max = max(self.max, index)

    def find(self, number: int) -> int:
        i = 0
        while i < self.max:
            if i in self.d and self.d[i] == number:
                return i
            i+=1
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)