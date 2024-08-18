# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def height(root):
            nonlocal ans
            if root == None:
                return 0

            if root.left == root.right == None:
                return 0

            curr_max = l = r = 0

            if root.left != None:
                l = height(root.left)
                curr_max += l + 1

            if root.right != None:
                r = height(root.right)
                curr_max += r + 1

            ans = max(ans, curr_max)

            return 1 + max(l, r)

        height(root)

        return ans