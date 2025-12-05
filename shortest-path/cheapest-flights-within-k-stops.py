class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        for ori, to, price in flights:
            graph[ori].append((to, price))

        queue = deque([(0, src, 0)])
        best = defaultdict(lambda: inf)
        best[(src, 0)] = 0
        visited = set()
        ans = inf

        while queue:
            curr_price, city, curr_k = queue.popleft()

            if city == dst:
                ans = min(curr_price, ans)
                continue

            if curr_k == k + 1:
                continue

            for neigh, price in graph[city]:
                new_k = curr_k + 1
                new_price = curr_price + price

                if best[(neigh, new_k)] > new_price:
                    best[(neigh, new_k)] = new_price
                    queue.append((new_price, neigh, new_k))

        return -1 if ans == inf else ans


