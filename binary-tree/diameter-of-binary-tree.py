# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def find(root):
            nonlocal ans

            if not root:
                return 0

            l = find(root.left)
            r = find(root.right)

            ans = max(ans, l + r)
            # print(root.val, l, r)

            return max(l, r) + 1

        ans = 0
        find(root)
        return ans