import math
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix
        dist = [[math.inf] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
        # Fill in the distances from the given edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Floyd-Warshall Algorithm to find all-pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Count the number of reachable cities within the distanceThreshold for each city
        min_reachable_count = float('inf')
        best_city = -1
        
        for i in range(n):
            reachable_count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            if reachable_count <= min_reachable_count:
                min_reachable_count = reachable_count
                best_city = i
        
        return best_city
