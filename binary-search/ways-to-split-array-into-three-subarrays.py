class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        s, n = sum(nums), len(nums)

        MOD = 10 ** 9 + 7        
        prefix = []
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            prefix.append(curr)

        ans = 0
        for i in range(n):
            k1 = bisect_left(prefix, 2 * prefix[i])
            k2 = bisect_right(prefix, (prefix[i] + prefix[-1]) // 2)

            if k1 >= k2:
                continue

            ans += k2 - k1
            ans %= MOD

        return ans

        