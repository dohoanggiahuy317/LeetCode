class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1

        ans = 0
        
        for i in range(2, n):
            mean_num = n//i
            rem = n - i * mean_num

            ans = max(ans, (mean_num ** (i-1)) * (rem + mean_num))

            mean_num = n//i + 1
            rem = i * mean_num - n

            ans = max(ans, (mean_num ** (i-1)) * (mean_num - rem))



            # print((mean_num ** (i-1)) * (rem + mean_num), i, rem)

        return ans