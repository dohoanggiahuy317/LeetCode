class Solution:
    def minimumDeletions(self, s: str) -> int:
        suf_a = [0]*len(s)
        pre_b = [0]*len(s)

        suf_a[-1] = 0 if s[-1] == "a" else -1
        for i in range(len(s)-2, -1, -1):
            suf_a[i] = suf_a[i+1] + (1 if s[i] == "a" else 0)

        pre_b[0] = 0 if s[0] == "b" else -1
        for i in range(1, len(s)):
            pre_b[i] = pre_b[i-1] + (1 if s[i] == "b" else 0)

        # print(suf_a, pre_b)

        ans = min(pre_b[-1], suf_a[0])

        for i in range(1, len(s) - 1):
            ans = min(ans, pre_b[i] + suf_a[i])

        return ans + 1
                