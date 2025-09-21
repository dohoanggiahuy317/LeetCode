class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        

        graph = defaultdict(list)

        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        queue = deque([1])
        reachable = set(queue)
        ans = inf

        while queue:
            node = queue.popleft()

            for neigh, dist, in graph[node]:
                ans = min(ans, dist)
                if neigh in reachable:
                    continue
                queue.append(neigh)
                reachable.add(neigh)

        return ans

