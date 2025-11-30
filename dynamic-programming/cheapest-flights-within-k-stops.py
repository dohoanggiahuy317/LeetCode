class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
                
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))

        cost = [inf] * n
        cost[src] = 0

        queue = [(0, src, 0)]

        while queue:
            curr_price, city, curr_stop = heapq.heappop(queue)

            if city == dst and curr_stop <= k + 1:
                return curr_price
            
            if curr_stop == k + 1:
                continue

            for neighbor, p in graph[city]:
                if cost[neighbor] > curr_price + p:
                    cost[neighbor] = curr_price + p
                    heapq.heappush(queue, (cost[neighbor], neighbor, curr_stop + 1))

        return -1