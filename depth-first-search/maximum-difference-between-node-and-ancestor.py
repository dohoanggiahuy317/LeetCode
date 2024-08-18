# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, curr):
            nonlocal ans
            if root == None:
                return

            temp1 = []

            if root.left != None:
                for x in curr:
                    temp1.append(x + root.val - root.left.val)

                temp1.append(root.val - root.left.val)
                dfs(root.left, temp1)

            temp2 = []

            if root.right != None:
                for x in curr:
                    temp2.append(x + root.val - root.right.val)

                temp2.append(root.val - root.right.val)
                dfs(root.right, temp2)

            for x in temp1:
                ans = max(ans, abs(x))
            for x in temp2:
                ans = max(ans, abs(x))

        dfs(root, [])
        return ans