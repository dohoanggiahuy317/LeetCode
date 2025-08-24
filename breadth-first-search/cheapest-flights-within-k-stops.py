class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for s, d, cost in flights:
            graph[s].append((d, cost))


        visited = [[inf] * (k + 2) for _ in range(n)]
        visited[src][0] = 0
        pq = [(0, src, 0)]
        step = 0

        while pq:
            cost, u, s = heapq.heappop(pq)
            if u == dst:
                return cost
            if s == k + 1:
                continue

            for neigh, w in graph[u]:
                new = cost + w
                if new < visited[neigh][s + 1]:
                    visited[neigh][s + 1] = new
                    heapq.heappush(pq, (new, neigh, s + 1))

        return -1

