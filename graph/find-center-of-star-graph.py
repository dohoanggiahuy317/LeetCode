class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        nodes = [0] * (n + 1)
        center, max_edges = 0, 0

        for u, v in edges:
            nodes[u] += 1
            nodes[v] += 1

            if nodes[u] > max_edges:
                center, max_edges = u, nodes[u]
            
            if nodes[v] > max_edges:
                center, max_edges = v, nodes[v]
        
        return center
            