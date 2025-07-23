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
        if self.tail is None:
            self.tail = node

    def helper(self, key: int, node: NodeVal) -> int:
        cur = self.MAP.get(key)
        if cur:
            self.remove(cur)
        self.add_to_front(node)
        self.MAP[key] = node
        return node.val
        
    def get(self, key: int) -> int:
        if key not in self.MAP:
            return -1
        return self.helper(key, self.MAP[key])

    def put(self, key: int, value: int) -> None:
        if key not in self.MAP:
            self.length += 1
        self.helper(key, NodeVal(key, value))
        
        while self.length > self.capacity:
            temp = self.tail.pre

            temp.nex = None
            del self.MAP[self.tail.key]
            self.tail = temp

            self.length -= 1



        
