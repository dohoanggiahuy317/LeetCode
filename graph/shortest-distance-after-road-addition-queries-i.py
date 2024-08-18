from typing import List
import heapq

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def dijkstra(graph, start, end):
            pq = [(0, start)]
            distances = {i: float('inf') for i in range(n)}
            distances[start] = 0

            while pq:
                current_distance, current_node = heapq.heappop(pq)

                if current_distance > distances[current_node]:
                    continue

                for neighbor, weight in graph[current_node]:
                    distance = current_distance + weight

                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(pq, (distance, neighbor))

            return distances[end]

        graph = {i: [] for i in range(n)}
        for i in range(n - 1):
            graph[i].append((i + 1, 1))

        answer = []

        for ui, vi in queries:
            graph[ui].append((vi, 1)) 
            shortest_distance = dijkstra(graph, 0, n - 1)
            answer.append(shortest_distance)

        return answer