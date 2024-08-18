# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(node, currSum, path):
            nonlocal ans, targetSum

            if not node:
                return

            if not node.left and not node.right and currSum + node.val == targetSum:
                ans.append(path + [node.val])
                return

            dfs(node.left, currSum + node.val, path + [node.val])
            dfs(node.right, currSum + node.val, path + [node.val])

        ans = []
        dfs(root, 0, [])
        return ans