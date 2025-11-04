class TwoSum:

    def __init__(self):
        self.arr = Counter()

    def add(self, number: int) -> None:
        self.arr[number] += 1        

    def find(self, value: int) -> bool:
        for num in self.arr:
            other_num = value - num

            if other_num != num and other_num in self.arr:
                return True
            if other_num == num and self.arr[num] > 1:
                return True

        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)