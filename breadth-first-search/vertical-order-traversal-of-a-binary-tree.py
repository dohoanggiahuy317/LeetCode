# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(root, x, y):
            nonlocal columns, mi, ma

            if not root:
                return None

            mi = min(mi, y)
            ma = max(ma, y)
            columns[y].append((x, root.val))

            dfs(root.left, x + 1, y - 1)
            dfs(root.right, x + 1, y + 1)

        columns = defaultdict(list)
        mi = ma = 0
        dfs(root, 0, 0)
        
        ans = []
        for i in range(mi, ma + 1):
            ans.append([v[1] for v in sorted(columns[i])])

        return ans