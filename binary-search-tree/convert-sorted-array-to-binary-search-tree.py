# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])
        if len(nums) == 0:
            return None

        # mid = nums[len(nums)//2]

        # subl = nums[:len(nums)//2]
        # subr = nums[len(nums)//2 + 1:]

        root = TreeNode(nums[len(nums)//2])
        root.left = self.sortedArrayToBST(nums[:len(nums)//2])
        root.right = self.sortedArrayToBST(nums[len(nums)//2 + 1:])

        return root
