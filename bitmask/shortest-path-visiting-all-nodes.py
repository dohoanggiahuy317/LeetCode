class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        n = len(graph)
        ans = inf

        for start in range(n):

            queue = deque([(start, 1)])
            reachable = set(queue)
            found_all = False
            step = 0
            
            print("start", start)
            

            while queue and not found_all:
                # print(queue)
                # print(reachable)
                # print(step)
                for _ in range(len(queue)):
                    node, count = queue.popleft()
                    
                    if count == n:
                        ans = min(ans, step)
                        found_all = True
                        break

                    for neigh in graph[node]:
                        
                        new_count = count
                        if all((neigh, i) not in reachable for i in range(count)):
                            new_count = count + 1

                        if (neigh, new_count) in reachable:
                            continue

                        queue.append((neigh, new_count))
                        reachable.add((neigh, new_count))

                step += 1

        return 0 if ans == inf else ans


