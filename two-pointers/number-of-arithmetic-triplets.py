class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        d = Counter()

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] - nums[j] == diff:
                    d[i] += 1
                    ans += d[j]

        return ans



