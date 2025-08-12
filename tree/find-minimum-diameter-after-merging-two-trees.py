class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        START_ROOT = 0
        INIT_NUM_EDGES = -1

        def create_tree(edges):
            tree = defaultdict(list)
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            return tree

        def get_endpoint(tree, root):

            queue = deque([root])
            reachable = set(queue)
            endpoint = root
            num_edges = INIT_NUM_EDGES

            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    endpoint = curr

                    for neigh in tree[curr]:
                        if neigh in reachable:
                            continue
                        queue.append(neigh)
                        reachable.add(neigh)
                
                num_edges += 1
            
            return endpoint, num_edges

        def find_diameter(tree, root):            
            endpoint, _ = get_endpoint(tree, root)
            _, diameter = get_endpoint(tree, endpoint)
            return diameter

        tree1 = create_tree(edges1)
        tree2 = create_tree(edges2)

        b1_diameter = find_diameter(tree1, START_ROOT)
        b2_diameter = find_diameter(tree2, START_ROOT)

        return max([ b1_diameter, 
                     b2_diameter, 
                     (b1_diameter + 1) // 2 + (b2_diameter + 1) // 2 + 1
                    ])