from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for preq in prerequisites:
            graph[preq[1]].append(preq[0])

        # for u, v in graph.items():
        #     print(u, v)

        def dfs(curr_node, visited):
            nonlocal graph, cyc

            if cyc:
                return

            if visited[curr_node]:

                cyc = True
                return

            visited[curr_node] = True

            for neigh in graph[curr_node]:
                dfs(neigh, visited)

            visited[curr_node] = False

        for start in range(numCourses):
            visited = [False] * numCourses
            cyc = False

            dfs(start, visited)

            if cyc:
                return False

        return True

