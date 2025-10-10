class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2idx = {num: idx for idx, num in enumerate(nums)}

        for i, num in enumerate(nums):
            if target - num in nums2idx and nums2idx[target - num] != i:
                return [i, nums2idx[target - num] ]

        return []