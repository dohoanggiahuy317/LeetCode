# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    li = []

    def transversal(self, root):
        if root == None:
            return
        self.li.append(root.val)

        self.transversal(root.left)
        self.transversal(root.right)

        return


    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.li = []

        self.transversal(root)

        sl = sorted(self.li)

        m = sl[1] - sl[0]

        for i in range(1, len(sl)):
            if sl[i] - sl[i-1] < m:
                m = sl[i] - sl[i-1]

        return m
