class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def add_number(pick_stats, curr_li):
            nonlocal n, ans

            if len(curr_li) == n:
                ans.add(tuple(curr_li[:]))
                return
            
            for i, pick in enumerate(pick_stats):
                if not pick:
                    pick_stats[i] = True
                    add_number(pick_stats, curr_li + [nums[i]])
                    pick_stats[i] = False

        n = len(nums)
        ans = set()
        add_number([False] * n, [])
        return [list(permu) for permu in ans]
