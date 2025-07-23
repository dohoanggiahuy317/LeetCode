class NodeVal:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.freqval = None
        self.freq = 1
        self.pre = None 
        self.nex = None

class FreqVal:
    def __init__(self, freq: int):
        self.freq = freq
        self.head = None
        self.tail = None
        self.pre = None 
        self.nex = None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.MAP = {}
        self.freq_head = None 

    def remove_node(self, bucket, node):
        if node.pre:
            node.pre.nex = node.nex
        else:
            bucket.head = node.nex

        if node.nex:
            node.nex.pre = node.pre
        else:
            bucket.tail = node.pre

        node.pre = node.nex = None

        if not bucket.head:
            self.remove_bucket(bucket)

    def add_node(self, bucket, node):
        node.pre = None
        node.nex = bucket.head
        if bucket.head:
            bucket.head.pre = node
        bucket.head = node
        if not bucket.tail:
            bucket.tail = node
        node.freqval = bucket

    def remove_bucket(self, bucket):
        if bucket.pre:
            bucket.pre.nex = bucket.nex
        else:
            self.freq_head = bucket.nex

        if bucket.nex:
            bucket.nex.pre = bucket.pre
        bucket.pre = bucket.nex = None

    def add_bucket(self, prevb, newb):
        if not prevb:
            newb.nex = self.freq_head
            if self.freq_head:
                self.freq_head.pre = newb
            self.freq_head = newb
        else:
            newb.pre = prevb
            newb.nex = prevb.nex
            if prevb.nex:
                prevb.nex.pre = newb
            prevb.nex = newb

    def get(self, key: int) -> int:
        if key not in self.MAP:
            return -1

        node = self.MAP[key]
        bucket = node.freqval

        self.remove_node(bucket, node)
        node.freq += 1

        bucket_nex = bucket.nex
        if not bucket_nex or bucket_nex.freq != node.freq:
            bucket_nex = FreqVal(node.freq)
            self.add_bucket(bucket, bucket_nex)

        self.add_node(bucket_nex, node)
        if not self.freq_head:
            self.freq_head = bucket_nex
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.MAP:
            node = self.MAP[key]
            node.val = value
            self.get(key)
            return

        if self.length >= self.capacity:
            print(self.length)
            print(self.freq_head)

            last_node = self.freq_head.tail
            self.remove_node(self.freq_head, last_node)
            del self.MAP[last_node.key]
            self.length -= 1
        
        node = NodeVal(key, value)
        
        self.MAP[key] = node
        self.length += 1

        if not self.freq_head or self.freq_head.freq != 1:
            self.add_bucket(None, FreqVal(1))
        self.add_node(self.freq_head, node)

        # print("put", key, value, self.length)
        