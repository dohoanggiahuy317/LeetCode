class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def get_new_num(i, curr_li, curr_sum):
            nonlocal candidates, ans, n

            if curr_sum == target:
                ans.append(curr_li[:])
                return

            if curr_sum > target:
                return

            for j in range(i, len(candidates)):
                cand = candidates[j]
                get_new_num(j, curr_li + [cand], curr_sum + cand)


        n = len(candidates)
        ans = []
        get_new_num(0, [], 0)
        return ans