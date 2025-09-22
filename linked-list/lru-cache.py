class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.key2val = {}
        self.cache_head, self.cache_tail = None, None

    def pop_out(self, node):
        prev_node = node.prev
        next_node = node.next

        # handle prev_node
        if prev_node:
            prev_node.next = next_node
        else:
            self.cache_head = next_node

        # handle next_node
        if next_node:
            next_node.prev = prev_node
        else:
            self.cache_tail = prev_node

        # Handle node
        node.prev = None
        node.next = None

    def update_cache_head(self, node):
        node.next = self.cache_head
        if self.cache_head:
            self.cache_head.prev = node
        
        self.cache_head = node

        if not self.cache_tail:
            self.cache_tail = node

    def update_cache_tail(self):
        if not self.cache_tail:
            return

        # Detach the tail
        tail = self.cache_tail
        self.cache_tail = tail.prev
        if self.cache_tail:
            self.cache_tail.next = None
        tail.prev = None

        # del the key
        key = tail.key
        del self.key2val[key]

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        # get node
        node = self.key2val[key]
        self.pop_out(node)
        self.update_cache_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        
        if key in self.key2val:
            node = self.key2val[key]
            self.pop_out(node)
            node.val = value
        else:
            node = Node(key, value)
            self.key2val[key] = node
        
            if self.size == self.cap:
                self.update_cache_tail()
                self.size -= 1

            self.size += 1
        
        self.update_cache_head(node)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)