class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 0:
            return nums

        ans = [-1] * n
        if 2 * k + 1 > n:
            return ans

        curr_sum = sum(nums[:(2 * k + 1)])
        ans[k] = curr_sum // (2 * k + 1)

        for i in range(n):
            if i - k <= 0 or i + k >= n:
                continue


            curr_sum += nums[i + k]
            curr_sum -= nums[i - k - 1]
            ans[i] = curr_sum // (2 * k + 1)


        return ans

