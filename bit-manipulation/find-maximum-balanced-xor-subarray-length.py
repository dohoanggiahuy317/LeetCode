class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        parity = [0] * n
        prefix_xor = [0] * n
        seen = {(0, 0): -1}
        ans = 0
        
        for j, num in enumerate(nums):
            prefix_xor[j] = num ^ (prefix_xor[j - 1] if j > 0 else 0)
            parity[j] = (1 if num % 2 else -1) + (parity[j - 1] if j > 0 else 0)

            key = (prefix_xor[j], parity[j])
            if key not in seen:
                seen[key] = j
            else:
                i = seen[key]
                ans = max(ans, j - i)

        return ans