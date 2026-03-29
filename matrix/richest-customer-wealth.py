class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = -inf

        for acc in accounts:
            max_sum = max(max_sum, sum(acc))

        return max_sum