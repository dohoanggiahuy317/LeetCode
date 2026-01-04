# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def count(self, node, curr, tar):
        if not node:
            return 0

        cnt = 1 if curr + node.val == tar else 0
        cnt += self.count(node.left, curr + node.val, tar)
        cnt += self.count(node.right, curr + node.val, tar)
        return cnt

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        return self.count(root, 0, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)