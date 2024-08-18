class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        
        prefSum = {-1: 0}
        for i, v in enumerate(nums):
            prefSum[i] = prefSum[i-1] + nums[i]
        
        for i, v in enumerate(nums):
            new_i = i
            while stack and stack[-1][0] > v:
                pop_v, pop_i = stack.pop(-1)
                ans = max(ans, pop_v * (prefSum[i-1] - prefSum[pop_i-1]))
                new_i = pop_i

            stack.append((v, new_i))

        for v, i in stack:
            ans = max(ans, v * (prefSum[len(nums) - 1] - prefSum[i-1]) )

        return ans % (10**9 + 7)