class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (n + len(rolls))
        n_sum = total - sum(rolls)

        if n_sum > 6 * n or n_sum < n:
            return []

        ave = n_sum // n
        left = n_sum - ave * n
        ans = []

        for x in range(n):
            ans.append(ave)

        for i in range(left):
            ans[i] += 1
        
        return ans

        