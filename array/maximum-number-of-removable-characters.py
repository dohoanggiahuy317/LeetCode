class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def check(p, smap):
            j = 0
            for i in range(len(smap)):
                if j == len(p):
                    break
                if smap[i][1] == p[j]:
                    j += 1

            return j == len(p)

        smap = defaultdict()
        for i, char in enumerate(s):
            smap[i] = char
        
        temp = [smap]
        for idx in removable:
            del smap[idx]
            temp.append(list(smap.items()))
        ans = 0

        l, r = 0, len(temp) - 1
        while l <= r:
            m = (l + r) // 2
            if check(p, temp[m]):
                ans = m
                l = m + 1
            else:
                r = m - 1

        return ans