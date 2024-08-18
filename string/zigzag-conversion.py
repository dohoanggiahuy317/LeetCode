class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        
        ans = ""

        for i in range(numRows):
            start = i
            while start < len(s):
                ans += s[start]
                start += (numRows - i - 1)*2
                if start < len(s) and i > 0 and i != numRows - 1:
                    ans += s[start]
                    start += i*2
                elif start < len(s) and i == numRows - 1:
                    start += i*2
                    

        return ans
