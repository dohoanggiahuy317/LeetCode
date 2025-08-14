

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Constant
        INIT_QUOTIENT = 1

        # BFS for each query
        def bfs(divider, divisor):
            nonlocal ans, eq_map

            queue = deque([(divider, INIT_QUOTIENT)])
            reachable = set([divider]) # -> dont want to divide smth twice
            result = -1

            while queue:
                for _ in range(len(queue)):
                    prev_divisor, prev_quotient = queue.popleft()

                    if prev_divisor not in eq_map: # prev_divisor not appear as divider 
                        break

                    if prev_divisor == divisor:
                        result = prev_quotient
                        break

                    for neigh, value in eq_map[prev_divisor]: 
                    # prev_divisor/neigh = value

                        if neigh in reachable:
                            continue
                        
                        # prev_divisor/neigh * neigh/neigh_of_neigh * ...
                        new_quotient = prev_quotient * value 
                        
                        queue.append((neigh, new_quotient))
                        reachable.add(neigh)

            ans.append(result)


        eq_map = defaultdict(list) # eq_map[x] -> (y, value) where x/y = value
        for (x, y), value in zip(equations, values):
            eq_map[x].append((y, value)) 
            eq_map[y].append((x, 1/value))

        ans = []
        # loop through query
        for divider, divisor in queries:
            bfs(divider, divisor)

        return ans