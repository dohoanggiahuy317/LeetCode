class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        appear = [False] * (n + 1)

        for num in nums:
            appear[num] = True

        ans = []
        for i in range(1, n + 1):
            if appear[i] == False:
                ans.append(i)

        return ans