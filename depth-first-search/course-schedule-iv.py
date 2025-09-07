class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        u2v = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)

        
        for u, _ in prerequisites:
            queue = deque([u])

            while queue:
                node = queue.popleft()

                for neigh in graph[node]:
                    if not u2v[u][neigh]:
                        u2v[u][neigh] = True
                        queue.append(neigh)

        return [u2v[u][v] for u, v, in queries]
