class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        curr = 0
        temp = 1


        i = 1
        while i < len(nums):
            if nums[i] - nums[curr] <= 2 * k:
                temp += 1
                i += 1
                continue
            else:
                if curr == i:
                    i += 1
                else:
                    ans = max(ans, temp)
                    temp = 1
                    curr += 1

        return max(ans, temp)