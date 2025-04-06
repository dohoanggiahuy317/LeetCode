class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1] * len(nums)
        track = [-1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        track[i] = j

        curr_max = 1
        curr_ind = 0

        for i in range(len(nums)):
            if curr_max < dp[i]:
                curr_max = dp[i]
                curr_ind = i

        ans = []
        while curr_ind != -1:
            ans.append(nums[curr_ind])
            curr_ind = track[curr_ind]

        

        return ans