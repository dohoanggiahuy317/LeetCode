class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        
        n = 0
        for x, y in edges:
            n = max(n, max(x, y))

        n += 1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, parent):
            sizes = []
            good = True
            total_size = 1 
            
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                subtree_size = dfs(neighbor, node)
                sizes.append(subtree_size)
                total_size += subtree_size
            
            if len(sizes) > 0 and len(set(sizes)) != 1:
                good = False
            
            if good:
                good_nodes[0] += 1
            
            return total_size

        good_nodes = [0]
        dfs(0, -1)
        
        return good_nodes[0]