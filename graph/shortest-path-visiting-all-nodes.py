class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        n = len(graph)
        ans = inf

        for start in range(n):

            queue = deque([(start, 1 << start)])
            reachable = set(queue) 
            step = 0
                
            while queue:
                for _ in range(len(queue)):
                    node, past_node = queue.popleft()
                    
                    if past_node == (1 << n) - 1:

                        ans = min(ans, step)

                    for neigh in graph[node]:
                        
                        present_node = past_node | (1 << neigh)
                        if (neigh, present_node) in reachable:
                            continue

                        queue.append((neigh, present_node))
                        reachable.add((neigh, present_node))

                step += 1

        return ans
#     4 - 5
#         |
# 0 - 1 - 6 - 7
#     |
#     2 - 3


     
