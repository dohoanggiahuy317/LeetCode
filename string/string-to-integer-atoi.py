class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        neg = -1 if s.startswith("-") else 1

        if neg != -1:
            s = s[1:] if s.startswith("+") else s
        else:
            s = s[1:] if s.startswith("-") else s

        temp = ""
        i = 0
        while i < len(s) and s[i].isdigit():
            temp += s[i]
            i += 1
        
        if not temp:
            return 0
        
        if int(temp) * neg > 2**31-1:
            return 2**31-1
        elif int(temp) * neg < -2**31:
            return -2**31

        return int(temp) * neg
        