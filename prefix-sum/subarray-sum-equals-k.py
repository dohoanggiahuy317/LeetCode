class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = Counter()
        d[0] = 1
        curr_sum = 0
        ans = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            diff = curr_sum - k
            if diff in d:
                ans += d[diff]
            
            d[curr_sum] += 1

        return ans

