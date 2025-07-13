# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        tree_map = defaultdict(list)
        max_height = 0

        def dfs(root, level):
            nonlocal tree_map, max_height
            if not root:
                return
            max_height = max(max_height, level)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
            tree_map[level].append(root.val)
            return

        dfs(root, 0)

        return [tree_map[i] for i in range(max_height, -1, -1)]
                        
