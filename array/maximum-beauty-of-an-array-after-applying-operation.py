class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        curr = 0
        temp = 1


        i = 1
        while i < len(nums):
            # print(curr, i, temp, ans)
            if curr == i:
                i += 1
                continue
            if nums[i] - nums[curr] <= 2 * k:
                temp += 1
                i += 1
                continue
        
            ans = max(ans, temp)
            temp -= 1
            curr += 1

        # print(curr, i, temp, ans)

        return max(ans, temp)