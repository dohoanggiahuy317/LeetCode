class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.child1 = self.child2 = None

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.d = {}
        for i in range(-1, n):
            self.d[i] = Node(i)
        
        for i, p in enumerate(parent):
            self.d[i].parent = self.d[p]
            if not self.d[p].child1:
                self.d[p].child1 = self.d[i]
            else: 
                self.d[p].child2 = self.d[i]

    def getKthAncestor(self, node: int, k: int) -> int:
        i = 0
        while node != -1 and i < k:
            node = self.d[node].parent.val
            i += 1
        return node

        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)