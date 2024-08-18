"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        graph = {}

        def bfs(node):
            if node.val in graph.keys():
                return

            graph[node.val] = []

            for neighbor in node.neighbors:
                graph[node.val].append(neighbor.val)

            for neighbor in node.neighbors:
                bfs(neighbor)

        bfs(node)
        node_li = {}
        new_node = Node(node.val)
        node_li[1] = new_node

        for x in graph.keys():
            if x != 1:
                node_li[x] = Node(x)
        
        for k, v in graph.items():
            for neighbor in v:
                node_li[k].neighbors.append(node_li[neighbor])

        return new_node