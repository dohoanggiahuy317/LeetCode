class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        snums = sorted(list([(num, i) for i, num in enumerate(nums)]))
        ans = [0] * len(nums)

        for j, (num, i) in enumerate(snums):
            ans[i] = j
            
            if j > 0:
                if num == snums[j - 1][0]:
                    ans[i] = ans[snums[j - 1][1]]

        return ans
