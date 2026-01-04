class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        n1_graph = [-1] * n
        n2_graph = [-1] * n

        def bfs(start, i):
            nonlocal n1_graph, n2_graph, edges

            queue = deque([start])
            reachable = set(queue)
            step = 0

            while queue:
                curr = queue.popleft()
                if i == 1:
                    n1_graph[curr] = step
                else:
                    n2_graph[curr] = step

                neigh = edges[curr]
                if neigh in reachable:
                    continue
                if neigh == -1:
                    continue

                queue.append(neigh)
                reachable.add(neigh)
                step += 1

            
        bfs(node1, 1)
        bfs(node2, 2)

        best = inf
        ans = -1

        for i in range(n):
            if n1_graph[i] != -1 and n2_graph[i] != -1:
                cand = max(n1_graph[i], n2_graph[i])
                if cand < best or (cand == best and (ans == -1 or i < ans)):
                    best = cand
                    ans = i


        return ans


