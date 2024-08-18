class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        head = [0] * numCourses

        for prereq in prerequisites:
            start = prereq[1]
            end = prereq[0]

            graph[start].append(end)
            head[end] += 1

        
        queue = deque()
        for i in range(numCourses):
            if head[i] == 0:
                queue.append(i)

        n0_visited = 0
        while queue:
            node = queue.popleft()
            n0_visited += 1

            for neighbor in graph[node]:
                head[neighbor] -= 1
                if head[neighbor] == 0:
                    queue.append(neighbor)

        return n0_visited == numCourses