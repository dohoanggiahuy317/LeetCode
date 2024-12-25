# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        q = [(root, 0)]

        while q:
            # print(q)
            curr, level = q.pop(0)

            if len(ans) < level + 1:
                ans.append(curr.val)
            else:
                ans[level] = max(ans[level], curr.val)

            if curr.left:
                q.append((curr.left, level + 1))
            if curr.right:
                q.append((curr.right, level + 1))

        return ans