from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        m = defaultdict(list)
        for a, b in prerequisites:
            m[b].append(a)
        
        def dfs(i):
            nonlocal visited, stack, m
            visited.add(i)

            for ne in m[i]:
                if ne not in visited:
                    dfs(ne)

            stack.append(i)

        visited = set()
        stack = []
        for i in range(numCourses):
            if i not in visited:
                dfs(i)

        return stack[::-1]