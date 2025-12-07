class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        def backtrack(arr_i):
            nonlocal found

            if found:
                return

            if arr_i == len(ans):
                if not found:
                    found = True
                    for x in ans:
                        u.append(x)
                    # print(u)
                return

            if ans[arr_i] != 0:
                backtrack(arr_i + 1)
            
            for num in range(n, 0, -1):
                if arr_i + num >= len(ans):
                    continue
                if ans[arr_i] != 0 or ans[arr_i + num] != 0:
                    continue
                if used[num]:
                    continue

                ans[arr_i] = num
                if num != 1:
                    ans[arr_i + num] = num
                used[num] = True
                
                backtrack(arr_i + 1)
                
                used[num] = False
                ans[arr_i] = 0
                if num != 1:
                    ans[arr_i + num] = 0

        ans = [0] * (2 * n - 1)
        used = [False] * (n + 1)
        found = False
        u = []

        backtrack(0)
        
        return u