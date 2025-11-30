class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for fr, to, price in flights:
            graph[fr].append((to, price))

        best = defaultdict(lambda: inf)
        
        best[(0, src)] = 0
        queue = [(0, 0, src)]

        while queue:
            curr_cost, curr_step, city = heapq.heappop(queue)

            if city == dst and curr_step <= k + 1:
                return curr_cost

            if curr_cost > best[(curr_step, city)]:
                continue

            if curr_step == k + 1:
                continue

            for neigh, price in graph[city]:
                if best[(curr_step + 1, neigh)] > curr_cost + price:
                    best[(curr_step + 1, neigh)] = curr_cost + price
                    heapq.heappush(queue, (curr_cost + price, curr_step + 1, neigh))

        return -1
