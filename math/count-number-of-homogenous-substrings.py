class Solution:
    def countHomogenous(self, s: str) -> int:
        curr = s[0]
        l = 1
        ans = 1

        for i in range(1, len(s)):
            # print(ans, curr, l)
            if s[i] == curr:
                l += 1
                ans += l                
            else:
                l = 1
                ans += 1
                curr = s[i]

            ans = ans % (10 ** 9 + 7)

        return ans
