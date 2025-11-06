# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        columns = defaultdict(list)
        min_x, max_x, t = inf, -inf, 0

        def dfs(root, x, y):
            nonlocal min_x, max_x, t

            if not root:
                return

            columns[x].append((y, t, root.val))
            t += 1
            min_x = min(x, min_x)
            max_x = max(x, max_x)

            dfs(root.left, x - 1, y + 1)
            dfs(root.right, x + 1, y + 1)

        ans = []
        dfs(root, 0, 0)

        for i in range(min_x, max_x + 1):
            ans.append([x[2] for x in sorted(columns[i])])

        return ans