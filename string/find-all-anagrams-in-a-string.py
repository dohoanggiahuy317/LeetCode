from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p = Counter(list(p))
        n = len(p)

        curr = Counter(list(s[:n]))
        ans = []
        if curr == cnt_p:
            ans.append(0)

        for i in range(1, len(s) - n + 1):
            # print(curr)
            curr[ s[i-1] ] -= 1
            curr[ s[i+n-1] ] += 1
            
            if curr[ s[i-1] ] <= 0:
                del curr[ s[i-1] ]
            if curr == cnt_p:
                ans.append(i)

        return ans

