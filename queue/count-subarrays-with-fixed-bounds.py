class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        mi, ma, thres = -1, -1, -1
        ans = 0

        for i in range(len(nums)):
            num = nums[i]

            if num < minK or num > maxK:
                thres = i
                continue

            if num == minK:
                mi = i
            if num == maxK:
                ma = i

            if thres < min(mi, ma):
                ans += (min(mi, ma) - (thres+1)) + 1
                # print(thres, mi, ma, i)

        return ans
            