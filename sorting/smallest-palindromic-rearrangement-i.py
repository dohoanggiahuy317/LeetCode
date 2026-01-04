from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        d = Counter(list(s))
        l = list(map(lambda x: (x[0], x[1]//2), d.items()))

        l.sort(key=lambda x: x[0])
        # print(l)

        ans = ""
        mid = ""

        while l:
            u, v = l.pop(0)
            ans += u * v
            if d[u] % 2 == 1:
                mid = u
        
        ans += mid + ans[::-1]

        return ans