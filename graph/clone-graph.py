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

        def getCopy(neigh):
            nonlocal tree_map

            if neigh not in tree_map:
                copy_neigh = Node(neigh.val)
                tree_map[neigh] = copy_neigh

            return tree_map[neigh]


        copy_node = Node(node.val)
        tree_map = {node: copy_node}
        queue = deque([(node, copy_node)])
        reachable = set([node])


        while queue:

            for _ in range(len(queue)):
                curr, copy_curr = queue.popleft()

                for neigh in curr.neighbors:

                    neigh_copy = getCopy(neigh)
                    copy_curr.neighbors.append(neigh_copy)

                    if neigh in reachable:
                        continue

                    queue.append((neigh, neigh_copy))
                    reachable.add(neigh)

        return copy_node