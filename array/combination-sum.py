class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(curr_sum, idx):
            nonlocal target

            if curr_sum >= target:
                if curr_sum == target:
                    ans.append(comb[:])
                return

            for i in range(idx, len(candidates)):
                comb.append(candidates[i])
                dfs(curr_sum + candidates[i], i)
                comb.pop()

        ans = []
        comb = []
        dfs(0, 0)

        return ans