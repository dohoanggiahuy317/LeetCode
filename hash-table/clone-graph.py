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

        # BFS
        copy_node = Node(node.val)
        tree_map = {node: copy_node}
        queue = deque([(node, copy_node)])

        while queue:
            for _ in range(len(queue)):
                curr, copy_curr = queue.popleft() # get the current node

                for neigh in curr.neighbors:

                    # only add the queue the node that is just created
                    if neigh not in tree_map:
                        tree_map[neigh] = Node(neigh.val)
                        queue.append((neigh, tree_map[neigh]))

                    # copy the neighbor to the current node
                    copy_curr.neighbors.append(tree_map[neigh])

        return copy_node