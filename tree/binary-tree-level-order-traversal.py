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

        ans = [[root.val]]
        q = [(root, 1)]

        while q:
            curr_node, level = q.pop(0)
            if len(ans) < level + 1 and (curr_node.left or curr_node.right):
                ans.append([])

            if curr_node.left:
                q.append((curr_node.left, level + 1))
                ans[-1].append(curr_node.left.val)
            if curr_node.right:
                q.append((curr_node.right, level + 1))
                ans[-1].append(curr_node.right.val)

        return ans

            


                
