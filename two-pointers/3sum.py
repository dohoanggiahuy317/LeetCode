class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        triplet = []
        for i, num in enumerate(nums):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -num
            j, k = i + 1, len(nums) - 1

            while j < k:
                if j + 1 < k and nums[j] == nums[j + 1]:
                    j += 1
                elif k - 1 > j and nums[k] == nums[k - 1]:
                    k -= 1
                else:
                    if nums[j] + nums[k] < target:
                        j += 1
                    elif nums[j] + nums[k] > target:
                        k -= 1
                    else:
                        triplet.append([num, nums[j], nums[k]])
                        j += 1
                        k -= 1

        return triplet

