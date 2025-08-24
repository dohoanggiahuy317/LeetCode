class MyQueue:

    def __init__(self):
        self.l1 = []
        self.l2 = []

    def push(self, x: int) -> None:
        self.l1.append(x)

    def pop(self) -> int:
        while self.l1:
            self.l2.append(self.l1.pop())
        
        k = self.l2.pop()

        while self.l2:
            self.l1.append(self.l2.pop())
        
        return k

    def peek(self) -> int:
        return self.l1[0]

    def empty(self) -> bool:
        return True if not self.l1 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()