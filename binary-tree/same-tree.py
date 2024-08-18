# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        r1, r2 = [], []
        def transversal(root, r):
            nonlocal r1, r2

            if root == None:
                if r == "1":
                    r1.append(root)
                else:
                    r2.append(root)
                return

            if r == "1":
                r1.append(root.val)
            else:
                r2.append(root.val)
            
            transversal(root.left, r)

            transversal(root.right, r)

        transversal(p, "1")
        transversal(q, "2")

        # print(r1, r2)

        return r1 == r2
