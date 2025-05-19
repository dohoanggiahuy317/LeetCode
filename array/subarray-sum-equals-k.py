class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            dp[i + 1] = dp[i] + nums[i]

        freq = Counter(dp)
        # print(freq)
        ans = 0

        for u, v in freq.items():
            if u + k in freq and k != 0:
                ans += freq[u+k] * freq[u]
            else:
                if -u in freq and u != 0:
                    ans += freq[u+k] * freq[u]
                elif u == 0:
                    ans += freq[u+k] * freq[u]
                
        return ans