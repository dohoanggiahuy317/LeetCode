class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            dp[i + 1] = dp[i] + nums[i]

        freq = Counter(dp[1:])
        print(dp, freq)
        ans = 0

        for u, v in freq.items():
            if k != 0:
                if u + k in freq and k != 0:
                    ans += freq[u+k] * freq[u]
                if u == k:
                    ans += freq[u]
            else:
                if u == 0:
                    ans += freq[u]
                else:
                    ans += freq[u] * (freq[u] - 1) // 2
            # else:
            #     if -u in freq and u != 0:
            #         ans += freq[u+k] * freq[u]
            #     elif u == 0:
            #         ans += freq[u+k] * freq[u]
                
        return ans