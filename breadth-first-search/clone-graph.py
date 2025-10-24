"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        

        def dfs(node, node_copy):
            if node.val in visited:
                return
            
            visited.add(node.val)

            for neighbor in node.neighbors:
                if neighbor.val not in copy_vertices:
                    copy_vertices[neighbor.val] = Node(neighbor.val)

                node_copy.neighbors.append(copy_vertices[neighbor.val])
                
                dfs(neighbor, copy_vertices[neighbor.val])

        node_copy = Node(node.val)
        visited = set()
        copy_vertices = {node.val: node_copy}
        dfs(node, node_copy)

        return node_copy