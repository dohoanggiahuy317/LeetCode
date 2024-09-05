class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        n_sum = mean * (n + len(rolls)) - sum(rolls)

        if n_sum > 6 * n or n_sum < n:
            return []

        ave = n_sum // n
        left = n_sum - ave * n
        ans = [ave + 1] * left + [ave] * (n-left)

        return ans

        