class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.head = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.count += 1
        self.queue[ (self.head + self.count - 1) % len(self.queue) ] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.count -= 1
        self.head = (self.head + 1) % len(self.queue)

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[ (self.head + self.count - 1) % len(self.queue) ]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == len(self.queue)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()