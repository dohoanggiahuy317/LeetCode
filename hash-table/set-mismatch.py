class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = [-1, -1]
        n = len(nums)

        for i in range(1, n + 1):
            if c[i] == 0:
                ans[1] = i
            if c[i] == 2:
                ans[0] = i

        return ans