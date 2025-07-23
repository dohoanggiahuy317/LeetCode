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

    def helper(self, key: int, node: NodeVal) -> int:        
        cur = self.MAP[key]
        if cur:
            pre, nex = cur.pre, cur.nex
            if pre:
                pre.nex = nex
            if nex:
                nex.pre = pre
            else:
                self.tail = pre

        self.MAP[key] = node
        node.nex = self.head
        if self.length == 1:
            self.head = node
            self.tail = node
            return node.val
        self.head.pre = node
        self.head = node
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
        

        
