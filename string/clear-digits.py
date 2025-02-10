class Solution:
    def clearDigits(self, s: str) -> str:
        ans = ""
        temp = 0

        for i in range(len(s)-1, -1, -1):
            if s[i].isdigit():
                temp += 1
            
            else:
                if temp > 0:
                    temp -= 1
                else:
                    ans += s[i]

        return ans[::-1]