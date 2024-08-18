class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        leaves = deque()
        for node, neighbors in graph.items():
            if len(neighbors) == 1:  # leaf nodes
                leaves.append(node)

        while n > 2:
            num_leaves = len(leaves)
            n -= num_leaves

            for _ in range(num_leaves):
                leaf = leaves.popleft()
                neighbor = graph[leaf][0]
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:  # new leaf node
                    leaves.append(neighbor)

        return list(leaves)