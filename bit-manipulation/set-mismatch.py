class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = []
        n = len(nums)

        for i in range(1, n):
            if c[i] == 0 or c[i] == 2:
                ans.append(i)

        return ans