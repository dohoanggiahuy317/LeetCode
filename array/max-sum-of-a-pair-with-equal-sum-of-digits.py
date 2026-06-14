class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = -inf
        digit_map = defaultdict(lambda: -inf)

        for num in nums:
            sum_digit = sum(map(int, str(num)))
            ans = max(ans, num + digit_map[sum_digit])
            digit_map[sum_digit] = max(digit_map[sum_digit], num)
        
        return ans if ans != -inf else -1