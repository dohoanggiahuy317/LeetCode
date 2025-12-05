class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        for ori, to, price in flights:
            graph[ori].append((to, price))

        queue = [(0, 0, src)]
        best = defaultdict(lambda: inf)
        best[(src, 0)] = 0

        while queue:
            curr_price, curr_k, city = heapq.heappop(queue)

            if city == dst and curr_k <= k + 1:
                return curr_price

            if curr_k == k + 1:
                continue

            for neigh, price in graph[city]:
                new_k = curr_k + 1
                new_price = curr_price + price

                if best[(neigh, new_k)] > new_price:
                    best[(neigh, new_k)] = new_price
                    heapq.heappush(queue, (new_price, new_k, neigh))

        return -1


