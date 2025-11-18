class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        transmit_cost = [inf] * (n + 1)
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        queue = [(0, k)]
        transmit_cost[k] = 0
        
        while queue:
            cost, node = heapq.heappop(queue)

            if cost > transmit_cost[node]:
                continue

            for neigh, neigh_cost in graph[node]:
                new_cost = cost + neigh_cost
                if new_cost < transmit_cost[neigh]:
                    transmit_cost[neigh] = new_cost
                    heapq.heappush(queue, (new_cost, neigh))

        return max(transmit_cost[1:]) if all(cost != inf for cost in transmit_cost[1:]) else -1


