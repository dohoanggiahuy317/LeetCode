class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_or = set(list(order))

        pref = ""
        d = {}
        for char in list(s):
            if char in s_or:
                if char in d:
                    d[char] += 1  
                else:
                    d[char] = 1
            else:
                pref += char
        
        ans = ""
        for char in list(order):
            if char in d:
                ans += char * d[char]

        return ans + pref

