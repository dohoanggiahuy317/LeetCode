class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        curr_min = float("INF")

        ans = []
        for c in cost:
            curr_min = min(c, curr_min)
            ans.append(curr_min)
        return ans