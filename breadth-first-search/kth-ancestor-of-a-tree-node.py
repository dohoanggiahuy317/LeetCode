class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.LOG = n.bit_length()
        self.dp = [[-1] *self.LOG for _ in range(n)]

        for i in range(n):
            self.dp[i][0] = parent[i]

        for j in range(1,self.LOG):
            for i in range(n):
                prev = self.dp[i][j - 1]
                self.dp[i][j] = -1 if prev < 0 else self.dp[prev][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:

        for j in range(self.LOG):
            if k & (1 << j):
                node = self.dp[node][j]
                if node < 0:
                    return -1
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)