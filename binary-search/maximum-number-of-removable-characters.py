class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def check(k):
            nonlocal p, s
            removed = set(removable[:k])
            j = 0
            for i, ch in enumerate(s):
                if i in removed:
                    continue
                if j < len(p) and ch == p[j]:
                    j += 1
                    if j == len(p):
                        break
            return j == len(p)
        
        ans = 0
        l, r = 0, len(removable)
        while l <= r:
            m = (l + r) // 2

            if check(m):
                ans = m
                l = m + 1
            else:
                r = m - 1

        return ans