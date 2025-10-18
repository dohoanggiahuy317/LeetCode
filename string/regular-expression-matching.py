class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        ls = len(s)
        lp = len(p)

        dp = defaultdict()

        def match(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            if j == lp:
                return i == ls

            char_match = i < ls and (p[j] == "." or p[j] == s[i])

            if j < lp - 1 and p[j + 1] == "*":
                dp[(i, j)] = match(i, j + 2) or (char_match and match(i + 1, j))
            else:
                dp[(i, j)] = char_match and match(i + 1, j + 1)
        
            return dp[(i, j)]
        
        match(0, 0)

        return dp[(0, 0)]
