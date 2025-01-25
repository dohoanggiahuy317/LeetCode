class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        
        MOD = 10**9 + 7

        frac = list(accumulate(range(1, 10**5 + 1), lambda x, y: x * y % M, initial=1))

        
        def combina(n, k):
            nonlocal MOD
            if n < k:
                return 0
            return frac[n] * pow(frac[k], -1, MOD) * pow(frac[n-k], -1, MOD) % MOD
        
        nums.sort()
        n = len(nums)
        ans = 0
        temp = 1


        for i in range(len(nums)):
            ans += (nums[i] + nums[n-i-1]) * temp
            ans %= MOD
            temp = (2 * temp - comb(i, k-1)) % MOD


        return ans % MOD