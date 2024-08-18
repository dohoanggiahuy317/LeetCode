class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans = 0

        for x in nums:
            if x == 1:
                count += 1
                ans = max(ans, count)

            else:
                count = 0

        return ans