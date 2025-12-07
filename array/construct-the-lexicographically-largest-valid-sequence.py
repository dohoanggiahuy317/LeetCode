
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        def backtrack(i: int):
            nonlocal found, result

            if found:
                return

            if i == len(ans):
                found = True
                result = ans[:]
                return

            if ans[i] != 0:
                backtrack(i + 1)
                return

            for num in range(n, 0, -1):
                if used[num]:
                    continue

                if num == 1:
                    ans[i] = 1
                    used[1] = True

                    backtrack(i + 1)

                    used[1] = False
                    ans[i] = 0
                else:
                    j = i + num
                    if j >= len(ans) or ans[j] != 0:
                        continue

                    ans[i] = num
                    ans[j] = num
                    used[num] = True

                    backtrack(i + 1)

                    used[num] = False
                    ans[i] = 0
                    ans[j] = 0

        ans = [0] * (2 * n - 1)
        used = [False] * (n + 1)
        found = False
        result = []

        backtrack(0)
        return result