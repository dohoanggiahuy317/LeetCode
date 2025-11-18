class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        best = defaultdict(lambda: inf)
        
        graph = [[] for _ in range(n)]
        for f, t, p in flights:
            graph[f].append((t, p))

        queue = [(0, 0, src)]
        best[(0, src)] = 0

        while queue:
            cost, step, city = heapq.heappop(queue)

            if city == dst:
                return cost

            if cost > best[city]:
                continue

            if step == k + 1:
                continue

            for neigh_city, neigh_cost in graph[city]:
                new_cost = cost + neigh_cost
                if (step, neigh_city) not in best:
                    
                    best[(step, neigh_city)] = new_cost
                    heapq.heappush(queue, (new_cost, step + 1, neigh_city))


        return -1