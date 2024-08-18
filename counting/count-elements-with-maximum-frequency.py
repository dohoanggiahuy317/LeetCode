class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cur = 0
        ans = 0
        d = {}

        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1

            if d[x] > cur:
                cur = d[x]
                ans = 0
                ans += cur
            elif d[x] == cur:
                ans += cur
            
        return ans