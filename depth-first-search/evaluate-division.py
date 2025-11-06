class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), v in zip(equations, values):
            graph[a].append((b, v)) # a / b = value
            graph[b].append((a, 1/v)) # b / a = 1/value

        def bfs(c, d):
            nonlocal graph

            if c not in graph or d not in graph:
                return -1

            queue = deque([(c, 1)])
            visited = set([c])

            while queue:
                for _ in range(len(queue)):
                    node, val = queue.popleft()

                    if node == d:
                        return val

                    for neigh, neigh_val in graph[node]:
                        if neigh in visited:
                            continue
                        
                        queue.append((neigh, val * neigh_val))
                        visited.add(neigh)

            return -1

        ans = []
        for c, d in queries:
            ans.append(bfs(c, d))

        return ans