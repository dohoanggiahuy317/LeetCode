class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def get_new_num(curr_li, curr_sum):
            nonlocal candidates, ans, n

            if curr_sum == target:
                ans.add(tuple(sorted(curr_li)))
                return

            if curr_sum > target:
                return

            for cand in candidates:
                get_new_num(curr_li + [cand], curr_sum + cand)


        n = len(candidates)
        ans = set()
        get_new_num([], 0)
        return [list(x) for x in ans]