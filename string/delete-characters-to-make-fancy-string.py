class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ""
        curr, count = "", 0
        for ch in s:
            if ch == curr and count == 2:
                continue

            ans += ch
            
            if ch == curr:
                count += 1
            else:
                curr = ch
                count = 1

        return ans
            
