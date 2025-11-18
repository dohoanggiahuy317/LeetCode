class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        n = len(graph)
        ALL_VISITED = (1 << n) - 1

        queue = deque([(i, 1 << i) for i in range(n)])
        visited = set(queue)
        step = 0

        while queue:
            for _ in range(len(queue)):
                node, state = queue.popleft()
                
                if state == ALL_VISITED:
                    return step

                for neigh in graph[node]:
                    new_state = state | (1 << neigh)

                    if (neigh, new_state) in visited:
                        continue
                    
                    queue.append((neigh, new_state))
                    visited.add((neigh, new_state))
            step += 1
            
        return -1