class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        triplet = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            k = len(nums) - 1
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                while k > j + 1 and nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                
                if k > j and nums[i] + nums[j] + nums[k] == 0:
                    triplet.append([nums[i], nums[j], nums[k]])   

        return triplet

