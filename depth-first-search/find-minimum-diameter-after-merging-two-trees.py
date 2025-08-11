class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def calculating_height(tree, root):
            queue = deque([root])
            reachable = set(queue)
            height = 0
            
            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    for neigh in tree[curr]:
                        if neigh in reachable:
                            continue
                        queue.append(neigh)
                        reachable.add(neigh)
                height += 1

            return height - 1
        
        def create_tree(edges):
            tree = defaultdict(list)
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            return tree

        tree1 = create_tree(edges1)
        tree2 = create_tree(edges2)
        min_height1 = min_height2 = inf
        
        for root1 in tree1.keys():
            height = calculating_height(tree1, root1)
            # print(root1, height)
            min_height1 = min(height, min_height1)
        for root2 in tree2.keys():
            height = calculating_height(tree2, root2)
            min_height2 = min(height, min_height2)
        
        return min_height1 + min_height2 + 1