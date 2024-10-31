from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        d = Counter(list(s))
        h = []
        ans = ""
        prev = None
        for u, v in d.items():
            heappush(h, (-v, u))

        while h or prev:
            if not h and prev:
                return ""
            
            v, u = heappop(h)

            ans += u
            v = -v
            v -= 1

            if prev:
                heappush(h, prev)
                prev = None
            if v != 0:
                prev = (-v, u)
                


        return ans