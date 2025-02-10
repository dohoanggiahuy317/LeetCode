class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def add_edge(u, v):
            nonlocal graph
            graph.append([u, v, abs(u[0] - v[0]) + abs(u[1] - v[1])])

        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent, rank, x, y):
            if rank[x] < rank[y]:
                parent[x] = y
            elif rank[x] > rank[y]:
                parent[y] = x
            else:
                parent[y] = x
                rank[x] += 1

        res = 0
        i, e = 0, 0
        graph = []
        parent, rank = {}, {}

        for i in range(len(points)-1):
            for j in range(len(points)):
                add_edge(tuple(points[i]), tuple(points[j]))

        graph.sort(key = lambda x: x[2])

        for node in points:
            parent[tuple(node)] = tuple(node)
            rank[tuple(node)] = 0

        # print(parent, rank, graph)

        while e < len(points) - 1:
            u, v, w = graph[i]
            i += 1
            x = find(parent, u)
            y = find(parent, v)

            if x!=y:
                e += 1
                res += w
                union(parent, rank, x, y)

        return res