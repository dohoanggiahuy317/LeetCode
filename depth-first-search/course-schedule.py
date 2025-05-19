from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for preq in prerequisites:
            graph[preq[1]].append(preq[0])

        def dfs(curr_node):
            nonlocal visited, graph, cyc

            if cyc:
                return

            if visited[curr_node]:
                cyc = True
                return

            visited[curr_node] = True

            for neigh in graph[curr_node]:
                dfs(neigh)

        for start in range(numCourses):
            visited = [False] * numCourses
            cyc = False

            dfs(start)

            if cyc:
                return False

        return True

