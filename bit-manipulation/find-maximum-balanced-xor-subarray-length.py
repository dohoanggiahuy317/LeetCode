class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        parity = [0] * n
        

        for i, num in enumerate(nums):
            parity[i] = ((num % 2) * 2 - 1) + (parity[i - 1] if i > 0 else 0)

        prefix_xor = [0] * n
        lowest_idx = defaultdict(lambda: float("INF"))
        ans = 0
        # print(parity)
        

        for j, num in enumerate(nums):
            prefix_xor[j] = num ^ (prefix_xor[j - 1] if j > 0 else 0)

            lowest_idx[prefix_xor[j]] = min(lowest_idx[prefix_xor[j]], j)

            i = lowest_idx[prefix_xor[j]]
            if parity[j] == parity[i]:
                # print(i, j)
                ans = max(ans, j - i)

            if prefix_xor[j] == 0 and parity[j] == 0:
                ans = max(ans, j + 1)
        
            # print(prefix_xor)
            # print(lowest_idx)

        return ans