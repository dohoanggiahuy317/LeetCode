class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.exist = False

class MapSum:

    def __init__(self):
        self.root = TrieNode("^")
        self.node2val = defaultdict(int)
        

    def insert(self, key: str, val: int) -> None:
        node = self.root

        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]

        self.node2val[node] = val
        node.exist = True

    def sum(self, prefix: str) -> int:
        node = self.root

        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return 0

        queue = deque([node])
        ans = 0
        while queue:
            node = queue.popleft()

            if node.exist:
                ans += self.node2val[node]
            
            for neigh in node.children:
                queue.append(node.children[neigh])

        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)