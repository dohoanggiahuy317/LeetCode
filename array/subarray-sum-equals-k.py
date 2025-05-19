class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            dp[i + 1] = dp[i] + nums[i]

        freq = []
        curr = 0
        cnt = 1

        for i in range(1, len(dp)):
            if dp[i] != curr:
                freq.append((curr, cnt))
                cnt = 1
                curr = dp[i]
            else:
                cnt += 1
        freq.append((curr, cnt))

        ans = 0
        # print(dp)
        # print(freq)
        if k == 0:
            for i in range(len(freq)):
                if freq[i][0] == 0 and i != 0:
                    ans += freq[i][1] * (freq[i][1] - 1) // 2
                for j in range(i+1, len(freq)):
                    if freq[j][0] - freq[i][0] == 0:
                        ans += freq[j][1] * freq[i][1]
        else:
            for i in range(len(freq)):
                for j in range(i+1, len(freq)):
                    if freq[j][0] - freq[i][0] == k:
                        ans += freq[j][1] * freq[i][1]
                
        return ans