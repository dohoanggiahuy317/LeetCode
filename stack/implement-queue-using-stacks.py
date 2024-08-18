class MyQueue:
    s1 = []
    s2 = []

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        while len(self.s1) > 0:
            x = self.s1.pop(len(self.s1) - 1)
            self.s2.append(x)

        a = self.s2.pop(len(self.s2) - 1)
        while len(self.s2) > 0:
            x = self.s2.pop(len(self.s2) - 1)
            self.s1.append(x)

        return a

    def peek(self) -> int:
        while len(self.s1) > 0:
            x = self.s1.pop(len(self.s1) - 1)
            self.s2.append(x)

        a = self.s2.pop(len(self.s2) - 1)
        self.s1.append(a)

        while len(self.s2) > 0:
            x = self.s2.pop(len(self.s2) - 1)
            self.s1.append(x)

        return a

    def empty(self) -> bool:
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()