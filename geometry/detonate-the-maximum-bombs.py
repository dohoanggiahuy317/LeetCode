class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j:
                    x1, y1, r1 = bombs[i]
                    x2, y2, r2 = bombs[j]

                    if (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r1 ** 2:
                        graph[i].append(j)

        
        def bfs(i):
            nonlocal ans, graph

            queue = deque([i])
            visited = set(queue)

            while queue:
                for _ in range(len(queue)):
                    this_bomb = queue.popleft()

                    for neigh_bomb in graph[this_bomb]:
                        if neigh_bomb in visited:
                            continue
                        queue.append(neigh_bomb)
                        visited.add(neigh_bomb)

            ans = max(ans, len(visited))

        ans = 1
        for i in range(n):
            bfs(i)

        return ans


