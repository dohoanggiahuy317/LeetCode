class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0,len(nums)-1):
            if sum(nums[:i+1]) >= sum(nums[i+1:]):
                ans += 1
        return(ans)
            