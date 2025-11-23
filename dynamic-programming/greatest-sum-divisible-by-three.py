class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)
        if s % 3 == 0:
            return s

        r1 = sorted([num for num in nums if num % 3 == 1])
        r2 = sorted([num for num in nums if num % 3 == 2])

        ans = 0

        if s % 3 == 1:
            if r1:
                ans = max(ans, s - r1[0])
            if len(r2) > 1:
                ans = max(ans, s - r2[0] - r2[1])
        
        if s % 3 == 2:
            if r2:
                ans = max(ans, s - r2[0])
            if len(r1) > 1:
                ans = max(ans, s - r1[0] - r1[1])
        # print(s)
        # print(ans)
        # print(r1)
        # print(r2)
        return ans