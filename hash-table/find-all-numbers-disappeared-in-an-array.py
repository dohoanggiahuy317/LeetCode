class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        s_nu = set(nums)
        for x in range(1, n + 1):
            if x not in s_nu:
                ans.append(x)

        return ans