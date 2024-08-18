class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(curr, remain):
            nonlocal ans, curr_li, candidates

            if remain == 0:
                ans.append(curr_li[:])

            for next_curr in range(curr, len(candidates)):
                if next_curr > curr and candidates[next_curr - 1] == candidates[next_curr]:
                    continue
                if remain - candidates[next_curr] < 0:
                    break

                curr_li.append(candidates[next_curr])
                helper(next_curr+1, remain - candidates[next_curr])
                curr_li.pop()

        candidates = list(filter(lambda x: x <= target, candidates))
        candidates.sort()
        curr_li = []

        ans = []
        helper(0, target)

        return ans

            