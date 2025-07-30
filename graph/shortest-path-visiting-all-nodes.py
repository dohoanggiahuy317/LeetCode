class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        ans = inf

        for start in range(n):
            queue = deque([(start, 1 << start)])
            reachable = set(queue)
            found_all = False # optimize by ending early
            step = 0
                
            while queue and not found_all: # optimize by ending early
                for _ in range(len(queue)):
                    node, past_path = queue.popleft()
                    
                    if past_path == (1 << n) - 1:
                        ans = min(ans, step)
                        found_all = True # optimize by ending early
                        break

                    for neigh in graph[node]:
                        
                        current_path = past_path | (1 << neigh)
                        if (neigh, current_path) in reachable:
                            continue

                        queue.append((neigh, current_path))
                        reachable.add((neigh, current_path))

                step += 1

        return ans



     
