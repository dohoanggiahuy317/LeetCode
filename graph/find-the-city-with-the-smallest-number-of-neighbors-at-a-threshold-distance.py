class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        def bfs(root):
            nonlocal graph, distanceThreshold, n

            pq = [(0, root)]
            dist = [inf] * n
            visited = [False] * n
            count = 0
            
            while pq:
                for _ in range(len(pq)):
                    curr_dist, node = heapq.heappop(pq)
                    visited[node] = True

                    for neigh, w in graph[node]:
                        
                        if visited[neigh]:
                            continue
                        
                        if dist[neigh] > curr_dist + w and distanceThreshold >= curr_dist + w:
                            dist[neigh] = curr_dist + w
                            heapq.heappush(pq, (dist[neigh], neigh))
            
            for x in visited:
                if x:
                    count += 1
            return count

        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        ans = -1
        curr = inf
        for i in range(n):
            c = bfs(i)
            # print(i, c - 1)
            # print("ans", ans, curr)
            if c <= curr:
                ans = i
                curr = c

        return ans
            
