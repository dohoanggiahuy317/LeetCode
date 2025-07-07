# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def _is_valid_bst(self, root):
        if not root:
            return -inf, inf, True

        max_left, min_left, is_left_bst = self._is_valid_bst(root.left)
        max_right, min_right, is_right_bst = self._is_valid_bst(root.right)

        check_order = max_left < root.val < min_right
        is_bst = check_order and is_left_bst and is_right_bst

        return max(max_right, root.val), min(min_left, root.val), is_bst

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._is_valid_bst(root)[2]