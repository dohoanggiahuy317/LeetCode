class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        # CONSTANT
        n = len(graph)
        src = 0
        dst = n - 1

        def parsing_node(x, curr_path):
            nonlocal adj_graph, ans, dst

            if x == dst:
                ans.append(curr_path[:])
                return

            for neigh in adj_graph[x]:
                parsing_node(neigh, curr_path + [neigh])

        
        # INIT
        adj_graph = {}
        for i, neighs in enumerate(graph):
            adj_graph[i] = neighs

        
        ans = []
        parsing_node(src, [src])
        return ans