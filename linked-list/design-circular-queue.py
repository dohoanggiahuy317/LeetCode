class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.size = 0
        self.head = None
        self.rear = None
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = Node(value)

        if self.isEmpty():
            self.head = new_node
            self.rear = new_node
        else:
            new_node.next = self.rear
            self.rear.prev = new_node
            self.rear = new_node
        
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        prev_node = self.head.prev
        if not prev_node:
            self.head = None
            self.rear = None
        else:
            self.head.prev = None
            prev_node.next = None
            self.head = prev_node
        
        self.size -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.head.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.rear.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.cap == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()