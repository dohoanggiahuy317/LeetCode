class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def check(p, s):
            j = 0
            for i in range(len(s)):
                if j == len(p):
                    break
                if s[i] == p[j]:
                    j += 1

            return j == len(p)

        removed_all = ""
        removeble_sor = sorted(removable)
        st = 0
        for i in range(len(s)):
            if st < len(removeble_sor) and i == removeble_sor[st]:
                st += 1
            else:
                removed_all += s[i]
        
        temp = []
        for idx in removable[::-1]:
            temp.append(removed_all)
            removed_all = removed_all[:idx] + s[idx] + removed_all[idx:]
            
        temp = [s] + temp[::-1]
        ans = 0

        l, r = 0, len(temp) - 1
        while l < r:
            m = (l + r) // 2
            if check(p, temp[m]):
                ans = m
                l = m + 1
            else:
                r = m - 1

        return ans