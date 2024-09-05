class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (n + len(rolls))
        n_sum = total - sum(rolls)

        if n_sum > 6 * n or n_sum < n:
            return []

        ave = n_sum // n

        ans = []

        for x in range(n-1):
            ans.append(ave)
            n_sum -= ave

        ans.append(n_sum)

        return ans

        