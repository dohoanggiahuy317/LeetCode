class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        n = len(graph)
        ans = inf

        map_dict = {}
        for i, neigh in enumerate(graph):
            map_dict[i] = neigh

        for start in range(n):

            queue = deque([(start, 0)])
            reachable = set(queue)
            s = 0
            found_all = False
            # print("start", start)
            

            while queue and not found_all:
                # print(queue)
                # print(reachable)
                for _ in range(len(queue)):
                    node, count = queue.popleft()

                    for neigh in map_dict[node]:
                        
                        if count + 1 == n:
                            ans = min(ans, s)
                            found_all = True
                            break
                        
                        new_count = count
                        if all((neigh, i) not in reachable for i in range(count)):
                            new_count = count + 1

                        if (neigh, new_count) in reachable:
                            continue

                        queue.append((neigh, new_count))
                        reachable.add((neigh, new_count))

                s += 1

        return 0 if ans == inf else ans


