class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []

        def backtrack(i, s):
            nonlocal target

            if s >= target:
                if s == target:
                    ans.append(curr[:])
                return

            for j in range(i, len(candidates)):
                x = candidates[j]
                
                curr.append(x)
                backtrack(j, s + x)
                curr.pop()

        backtrack(0, 0)
        return ans