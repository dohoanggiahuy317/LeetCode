class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        prev = s - nums[0] * len(nums)
        ans = [prev]

        for i in range(1, len(nums)):
            prev = prev - nums[i-1]*(i-1) + nums[i-1]*(len(nums)-i) - nums[i-1] + nums[i]*(i) - nums[i]*(len(nums)-(i+1)) - nums[i]
            ans.append(prev)

        return ans