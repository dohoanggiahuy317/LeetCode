class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        def create_tree(edges):
            tree = defaultdict(list)
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            return tree

        def find_diameter(tree, root):
            nonlocal visited, diameter
            if root in visited:
                return max(visited[root]) + 1

            visited[root] = [0, 0]
            for neigh in tree[root]:
                if neigh in visited:
                    continue
                child = find_diameter(tree, neigh)
                if child > visited[root][0]:
                    visited[root][1] = visited[root][0]
                    visited[root][0] = child
                elif child > visited[root][1]:
                    visited[root][1] = child

            diameter = sum(visited[root])
            return max(visited[root]) + 1

        tree1 = create_tree(edges1)
        tree2 = create_tree(edges2)
        b1_diameter = b2_diameter = 0

        visited = defaultdict(list)
        diameter = 0
        find_diameter(tree1, 0)
        b1_diameter = diameter
        
        visited = defaultdict(list)
        diameter = 0
        find_diameter(tree2, 0)
        b2_diameter = diameter

        return max([ b1_diameter, 
                     b2_diameter, 
                     (b1_diameter + 1) // 2 + (b2_diameter + 1) // 2 + 1
                    ])