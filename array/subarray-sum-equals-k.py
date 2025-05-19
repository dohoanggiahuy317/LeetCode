class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        curr = 0
        ans = 0

        for i in range(len(nums)):
            curr += nums[i]
            # print(left, i, curr, ans)

            while curr >= k and left <= i:
                if curr == k:
                    ans += 1
                curr -= nums[left]
                left += 1

            # print(left, i, curr, ans)
            # print()

        return ans