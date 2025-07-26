class Node:
    def __init__(self, value, key):
        self.prev = self.next = None
        self.val = value
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.head = self.tail = None
        self.capacity = capacity
        self.length = 0
        self.MAP = defaultdict(lambda: None)
    
    def helper(self, node):
        prev_node = node.prev
        next_node = node.next

        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        node.next  = node.prev = None

        if self.tail == node:
            self.tail = prev_node

        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

    def get(self, key: int) -> int:
        node = self.MAP[key]
        if node:
            self.helper(node)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        node = self.MAP[key]
        if node:
            node.val = value
            self.helper(node)
        else:
            while self.length >= self.capacity:
                last_node = self.tail
                prev_node = last_node.prev
                if prev_node:
                    prev_node.next = None
                del self.MAP[last_node.key]
                self.tail = prev_node
                self.length -= 1
                
            new_node = Node(value, key)
            self.helper(new_node)
            self.MAP[key] = new_node
            if self.length == 0:
                self.tail = new_node
            self.length += 1


            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)