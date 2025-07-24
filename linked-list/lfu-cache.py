class Node:
    def __init__(self, freq_val):
        self.pre = self.nex = None
        self.freq_val = freq_val
    
    def set_items(self, key, val, freq_node):
        self.key = key
        self.val = val
        self.freq_node = freq_node
    
    def set_bucket(self):
        self.head = self.tail = None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.MAP = {}
        self.freq_head = None 

    def remove_item(self, bucket, node):
        if node.pre:
            node.pre.nex = node.nex
        else:
            bucket.head = node.nex

        if node.nex:
            node.nex.pre = node.pre
        else:
            bucket.tail = node.pre

        if not bucket.head:
            self.remove_bucket(bucket)

    def add_item(self, bucket, node):
        node.pre = None
        node.nex = bucket.head # always add node to top of list
        if bucket.head:
            bucket.head.pre = node
        bucket.head = node # set the bucket head to this node
        if not bucket.tail:
            bucket.tail = node
        node.freq_node = bucket

    def remove_bucket(self, bucket):
        if bucket.pre:
            bucket.pre.nex = bucket.nex
        else:
            self.freq_head = bucket.nex

        if bucket.nex:
            bucket.nex.pre = bucket.pre
        # bucket.pre = bucket.nex = None

    def add_bucket(self, prevb, newb):
        if prevb:
            nextb = prevb.nex # get the next bucket to link
            newb.nex = nextb # insert the new bucket in
            newb.pre = prevb
            prevb.nex = newb # conect the previous bucket to new bucket
            if nextb: # connect the next bucket to new bucket
                nextb.pre = newb
        else:
            newb.nex = self.freq_head # connect new bucket to head
            if self.freq_head:
                self.freq_head.pre = newb
            self.freq_head = newb   # set the head to new bucket

    def get(self, key: int) -> int:
        if key not in self.MAP:
            return -1

        node = self.MAP[key]
        bucket = node.freq_node # get bucket info to jump to next bucket
        node.freq_val += 1
        self.remove_item(bucket, node)

        if not bucket.nex or bucket.nex.freq_val != node.freq_val:
            new_bucket = Node(node.freq_val)
            new_bucket.set_bucket()
            self.add_bucket(bucket, new_bucket)
        
        self.add_item(bucket.nex, node) 
        if not self.freq_head:
            self.freq_head = bucket.nex       
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.MAP: # if key alr in cache, just get it
            node = self.MAP[key]
            node.val = value
            self.get(key)
            return
        
        while self.length >= self.capacity:
            last_node = self.freq_head.tail
            self.remove_item(self.freq_head, last_node)
            del self.MAP[last_node.key]
            self.length -= 1

        node = Node(1) # new key that not in cache
        if not self.freq_head or self.freq_head.freq_val != 1: # if no bucket
            new_bucket = Node(1)
            new_bucket.set_bucket()
            self.add_bucket(self.freq_head, new_bucket)

        node.set_items(key, value, self.freq_head)  
        self.MAP[key] = node
        self.length += 1
        self.add_item(node.freq_node, node) # add node to head of 1st bucket


        