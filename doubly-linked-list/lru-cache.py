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

    def add_node(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        node.next = node.prev = None

        if node == self.head:
            self.head = next_node
        if node == self.tail:
            self.tail = prev_node

    def get(self, key: int) -> int:
        node = self.MAP[key]
        if node:
            self.remove_node(node)
            self.add_node(node)
            return node.val
            
        return -1
        
    def put(self, key: int, value: int) -> None:
        node = self.MAP[key]
        if node:
            node.val = value
            self.get(key)
        else:
            while self.length >= self.capacity:
                last_node = self.tail
                self.remove_node(last_node)
                del self.MAP[last_node.key]
                self.length -= 1
            
            new_node = Node(value, key)
            self.add_node(new_node)
            self.MAP[key] = new_node
            self.length += 1

            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)