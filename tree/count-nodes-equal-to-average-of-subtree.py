# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def count(n, i, e):
            nonlocal ans
            
            if n == None:
                return [0, 0]

            i1, e1 = count(n.left, i, e)
            i2, e2 = count(n.right, i, e)

            i = i + i1 + i2 + n.val
            e = e + e1 + e2 + 1

            if e > 0 and n.val == i//e:
                ans += 1

            return [i, e]

        count(root, 0, 0)
        return ans




        