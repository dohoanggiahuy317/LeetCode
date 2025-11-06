# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = defaultdict(list)
        min_x, max_x = inf, -inf

        def dfs(root, x, y):
            nonlocal min_x, max_x, columns

            if not root:
                return

            columns[x].append((y, root.val))
            min_x = min(x, min_x)
            max_x = max(x, max_x)

            dfs(root.left, x - 1, y + 1)
            dfs(root.right, x + 1, y + 1)

        dfs(root, 0, 0)
        ans = []
        for i in range(min_x, max_x + 1):
            # print(sorted(columns[i]))
            ans.append([ x[1] for x in sorted(columns[i]) ])
        # print(ans)

        return ans