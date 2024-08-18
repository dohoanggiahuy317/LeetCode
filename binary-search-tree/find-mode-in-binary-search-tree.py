# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def search(root):
            nonlocal d

            if root == None:
                return

            if root.val in d:
                d[root.val] += 1
            else:
                d[root.val] = 1

            search(root.left)
            search(root.right)

        
        d = {}
        search(root)

        ans = []
        curr = 0

        for x, y in d.items():
            if y > curr:
                ans = [x]
                curr = y
            elif y == curr:
                ans.append(x)

        return ans
        