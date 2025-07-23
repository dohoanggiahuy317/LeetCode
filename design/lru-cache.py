class NodeVal:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.nex, self.pre = None, None


class LRUCache:
    def __init__(self, capacity: int):
        self.MAP = defaultdict(lambda: None)
        self.length = 0
        self.head, self.tail = None, None
        self.capacity = capacity

    def remove(self, node):
        if node.pre:
            node.pre.nex = node.nex
        else:
            self.head = node.nex

        if node.nex:
            node.nex.pre = node.pre
        else:
            self.tail = node.pre

        node.pre = node.nex = None

    def add_to_front(self, node):
        node.pre  = None
        node.nex  = self.head
        if self.head:
            self.head.pre = node
        self.head  = node
        if not self.tail:
            self.tail = node
        
    def get(self, key: int) -> int:
        node = self.MAP[key]
        if not node:
            return -1
        self.remove(node)
        self.add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.MAP.get(key)
        if node:
            node.val = value
            self.remove(node)
            self.add_to_front(node)
        else:
            new_node = NodeVal(key, value)
            self.MAP[key] = new_node
            self.add_to_front(new_node)
            self.length += 1
        
        while self.length > self.capacity:
            temp = self.tail.pre

            temp.nex = None
            del self.MAP[self.tail.key]
            self.tail = temp

            self.length -= 1



        
