class Solution:
    def calculate(self, s: str) -> int:
        s += '+'  
        ans = 0           
        pending_num = 0
        creating_num = 0
        sign_before_creating_num = '+'

        for ch in s:
            if ch == ' ':
                continue
            if ch.isdigit():
                creating_num = creating_num * 10 + (ord(ch) - ord("0"))
            else:
                if sign_before_creating_num == '+':
                    ans += pending_num
                    pending_num = creating_num
                elif sign_before_creating_num == '-':
                    ans += pending_num
                    pending_num = -creating_num
                elif sign_before_creating_num == '*':
                    pending_num = pending_num * creating_num
                else:
                    val = pending_num / creating_num
                    pending_num = int(val) if val >= 0 else math.ceil(val)

                sign_before_creating_num = ch
                creating_num = 0

        return ans + pending_num