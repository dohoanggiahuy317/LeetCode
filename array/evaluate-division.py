INIT_QUOTIENT = 1

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        eq_map = defaultdict(list)
        for (x, y), value in zip(equations, values):
            eq_map[x].append((y, value))
            eq_map[y].append((x, 1/value))

        ans = []

        # loop through query
        for divider, divisor in queries:

            queue = deque([(divider, INIT_QUOTIENT)])
            reachable = set(queue)
            result = -1

            while queue:
                for _ in range(len(queue)):
                    node, prev_quotient = queue.popleft()

                    if node not in eq_map:
                        break

                    if node == divisor:
                        result = prev_quotient
                        break

                    for neigh, value in eq_map[node]:

                        if neigh in reachable:
                            continue
                        
                        new_quotient = prev_quotient * value
                        queue.append((neigh, new_quotient))
                        reachable.add(neigh)

            ans.append(result)

        return ans