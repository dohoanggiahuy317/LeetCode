class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplet = []
        for i in range(len(nums)):
            if not (i == 0 or nums[i] != nums[i - 1]):
                continue
            j = i + 1
            seen = set()
            while j < len(nums):
                target = - nums[i] - nums[j]

                if target in seen:
                    triplet.append([nums[i], nums[j], target])
                    while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 1
                
                seen.add(nums[j])
                j += 1

        return triplet
