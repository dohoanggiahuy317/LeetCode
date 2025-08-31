class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for dst, src in prerequisites:
            indegree[dst] += 1
            graph[src].append(dst)
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        ans = []

        while queue:   
            node = queue.popleft()
            ans.append(node)

            for neigh in graph[node]:
                indegree[neigh] -= 1

                if indegree[neigh] == 0:
                    queue.append(neigh)

        return ans