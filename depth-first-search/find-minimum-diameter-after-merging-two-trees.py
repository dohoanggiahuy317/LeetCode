class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        def create_tree(edges):
            tree = defaultdict(list)
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            return tree

        def get_best(tree, root):

            queue = deque([root])
            reachable = set(queue)
            best_node = root
            step = 0

            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    best_node = curr

                    for neigh in tree[curr]:
                        if neigh in reachable:
                            continue
                        queue.append(neigh)
                        reachable.add(neigh)
                
                step += 1
            
            return best_node, step - 1

        def find_diameter(tree, root):            
            first, _ = get_best(tree, root)
            sec, diameter = get_best(tree, first)
            # print(first, sec)

            return diameter

        tree1 = create_tree(edges1)
        tree2 = create_tree(edges2)
        b1_diameter = find_diameter(tree1, 0)
        b2_diameter = find_diameter(tree2, 0)
        # print(b1_diameter, b2_diameter)

        return max([ b1_diameter, 
                     b2_diameter, 
                     (b1_diameter + 1) // 2 + (b2_diameter + 1) // 2 + 1
                    ])