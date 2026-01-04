class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        n = len(nums)
        
        dp = [1] * n
        for i in range(n-2, -1, -1):
            if nums[i+1] == nums[i] + 1:
                dp[i] = dp[i+1] + 1

        # print(dp)
        results = []
        
        for i in range(n-k+1):
            is_consecutive = dp[i] >= k
            results.append(nums[i+k-1] if is_consecutive else -1)

        
        return results