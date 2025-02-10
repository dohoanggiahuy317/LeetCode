# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = [(root, 0)]
        ans = []

        while queue:
            curr, lvl = queue.pop(0)

            if lvl >= len(ans):
                ans.append([])
            ans[lvl].append(curr.val)

            if curr.left:
                queue.append((curr.left, lvl+1))
            if curr.right:
                queue.append((curr.right, lvl+1))

        return ans
