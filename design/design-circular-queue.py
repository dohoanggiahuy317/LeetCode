class MyCircularQueue:

    def __init__(self, k: int):
        self.l = [0] * k
        self.f = 0
        self.c = 0
        self.cnt = 0


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.l[(self.f + self.cnt) % len(self.l)] = value
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.f = (self.f + 1) % len(self.l)
        self.cnt -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.l[self.f]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.l[(self.f + self.cnt - 1) % len(self.l)]

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == len(self.l)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()