from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(dict)

        for u, v, w in times:
            graph[u][v] = w


        queue = []
        heapq.heappush(queue, (0, k))

        dist = [float("INF")] * n
        dist[k-1] = 0

        while queue:
            curr, node = heapq.heappop(queue)

            for neigh, weight in graph[node].items():
                if dist[neigh-1] > dist[node-1] + weight:
                    dist[neigh-1] = dist[node-1] + weight
                    heapq.heappush(queue, (dist[neigh-1], neigh))

        dist.pop(k-1)
        return max(dist) if float("INF") not in dist else -1