# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        left = False
        temp = [[root]]

        while temp[-1]:
            # print(temp)
            next_arr = []
            if left:
                for node in temp[-1]:
                    if node.left:
                        next_arr.append(node.left)
                    if node.right:
                        next_arr.append(node.right)

                left = not left
            else:

                for node in temp[-1][::-1]:
                    if node.right:
                        next_arr.append(node.right)
                    if node.left:
                        next_arr.append(node.left)

                left = not left
            temp.append(next_arr)

        ans = []

        for subarr in temp[:-1]:
            ans.append(list(map(lambda x: x.val, subarr)))

        return ans