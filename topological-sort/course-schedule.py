class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for a, b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)

        queue = deque([course for course in range(numCourses) if indegree[course] == 0])

        count = 0
        while queue:
            course = queue.popleft()
            count += 1

            for child in graph[course]:
                indegree[child] -= 1

                if indegree[child] == 0:
                    queue.append(child)

        return count == numCourses

