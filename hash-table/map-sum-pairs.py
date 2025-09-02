class TrieNode:
    def __init__(self, ch, val = -1):
        self.ch = ch
        self.children = {}
        self.exist = False
        self.val = val

class MapSum:

    def __init__(self):
        self.root = TrieNode("^")        

    def insert(self, key: str, val: int) -> None:
        node = self.root

        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]

        node.val = val
        node.exist = True

    def sum(self, prefix: str) -> int:
        node = self.root

        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return 0

        queue = deque([node]) # all the node with the prefix
        ans = 0
        while queue:
            node = queue.popleft()

            if node.exist:
                ans += node.val
            
            for neigh in node.children:
                queue.append(node.children[neigh])

        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)