class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1/v))

        def bfs(a, b):
            nonlocal graph, ans

            queue = deque([(a, 1)])
            reachable = set(queue)

            while queue:
                for _ in range(len(queue)):
                    curr, quot = queue.popleft()

                    if curr == b:
                        return quot

                    for neigh, neigh_quot in graph[curr]:
                        if neigh in reachable:
                            continue
                        new_quot = quot * neigh_quot
                        queue.append((neigh, new_quot))
                        reachable.add(neigh)

            return -1


        ans = []
        for a, b in queries:
            if a not in graph or b not in graph:
                ans.append(-1)
                continue
                
            v = bfs(a, b)
            ans.append(v)

        return ans
