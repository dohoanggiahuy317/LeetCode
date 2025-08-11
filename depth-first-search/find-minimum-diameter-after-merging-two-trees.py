class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def find_diameter(tree, root):
            nonlocal visited, diameter

            visited.add(root)
            best1 = best2 = 0
            
            for neigh in tree[root]:
                if neigh in visited:
                    continue
                child = find_diameter(tree, neigh)
                if child > best1:
                    best2 = best1
                    best1 = child
                elif child > best2:
                    best2 = child

            diameter = best1 + best2
            return max(best1, best2) + 1

        def create_tree(edges):
            tree = defaultdict(list)
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            return tree

        tree1 = create_tree(edges1)
        tree2 = create_tree(edges2)
        b1_diameter = b2_diameter = 0

        for root1 in tree1.keys():
            visited = set()
            diameter = 0
            find_diameter(tree1, root1)
            b1_diameter = max(b1_diameter, diameter)

        for root2 in tree2.keys():
            visited = set()
            diameter = 0
            find_diameter(tree2, root2)
            b2_diameter = max(b2_diameter, diameter)

        return max([ b1_diameter, 
                     b2_diameter, 
                     (b1_diameter + 1) // 2 + (b2_diameter + 1) // 2 + 1
                    ])