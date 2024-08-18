class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        

        pre_queue = deque()
        while queue:
            node = queue.popleft()
            pre_queue.append(node)

            for neighbor in graph[node]:
                head[neighbor] -= 1
                if head[neighbor] == 0:
                    queue.append(neighbor)

        if len(pre_queue) < numCourses:
            return []

        ans = []
        while pre_queue:
            ans.append(pre_queue.popleft())

        return ans