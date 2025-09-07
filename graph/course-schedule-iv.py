class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        ans = []

        for u, v in queries:
            queue = deque([u])
            reachable = set(queue)
            found = False

            while queue:
                node = queue.popleft()
                if node == v:
                    found = True
                    break

                for neigh in graph[node]:
                    queue.append(neigh)
            
            ans.append(found)

        return ans
