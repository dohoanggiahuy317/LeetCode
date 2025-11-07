"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        def dfs(node):
            nonlocal ptr

            while node:
                nxt = node.next

                ptr.next = node
                node.prev = ptr

                ptr = ptr.next

                if node.child:
                    dfs(node.child)

                node.child = None
                node = nxt


        ptr = Node(-1, None, None, None)
        mask = ptr
        
        dfs(head)

        ans = mask.next
        ans.prev = None
        return ans