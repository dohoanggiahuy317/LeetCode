from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        m = defaultdict(list)
        for a, b in prerequisites:
            m[b].append(a)

        def cyc(i):
            nonlocal rec_visit
            rec_visit.add(i)
            for ne in m[i]:
                if ne in rec_visit:
                    return False
                return cyc(ne)
                
            rec_visit.remove(i)
            return True

        for i in range(numCourses):
            rec_visit = set()
            if cyc(i) == False:
                return []

        
        def dfs(i):
            nonlocal visited, stack, m, b
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