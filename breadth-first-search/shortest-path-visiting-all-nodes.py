class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        ALL_VISITED = (1 << n) - 1

        queue = deque([(start, 1 << start) for start in range(n)])
        reachable = set(queue)
        step = 0
            
        while queue:
            for _ in range(len(queue)):
                node, past_path = queue.popleft()
                
                if past_path == ALL_VISITED:
                    return step

                for neigh in graph[node]:
                    
                    current_path = past_path | (1 << neigh)
                    if (neigh, current_path) in reachable:
                        continue

                    queue.append((neigh, current_path))
                    reachable.add((neigh, current_path))

            step += 1




     
