# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import Counter

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def trans(root, i):
            nonlocal d
            if root == None:
                return

            if i not in d:
                d[i] = 0
            d[i] += root.val
            trans(root.left, i + 1)
            trans(root.right, i + 1)

        d = Counter()
        trans(root, 0)
        l = sorted(list(d.values()), reverse = True)

        if k-1 >= len(l):
            return -1
        return l[k-1]