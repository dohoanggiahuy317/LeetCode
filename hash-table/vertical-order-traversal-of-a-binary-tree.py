# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(root, x, y):
            nonlocal tree_map, left, right

            if not root:
                return None

            left = min(left, y)
            right = max(right, y)

            tree_map[y].append((x, root.val))
            dfs(root.left, x + 1, y - 1)
            dfs(root.right, x + 1, y + 1)

        tree_map = defaultdict(list)
        left, right = 0, 0

        dfs(root, 0, 0)
        
        ans = []
        for i in range(left, right + 1):
            ans.append( [x[1] for x in sorted(tree_map[i])] )

        return ans