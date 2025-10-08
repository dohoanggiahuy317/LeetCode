class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        adj_graph = {i: neighs for i, neighs in enumerate(graph)}
        
        queue = deque([(src, 1 << src) for src in range(n)])
        visited = set(queue)
        step = 0

        while queue:
            for _ in range(len(queue)):
                node, k = queue.popleft()

                if k == (1 << n) - 1: #
                    return step

                for neigh in adj_graph[node]: #
                    new_k = k | (1 << neigh)
                    if (neigh, new_k) in visited:
                        continue
                    queue.append((neigh, new_k))
                    visited.add((neigh, new_k))

            step += 1

        return step