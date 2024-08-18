class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d_t = defaultdict(int)
        for char in list(t):
            d_t[char] += 1

        required = len(d_t)
        l, r = 0, 0

        window = defaultdict(int)
        form = 0
        min_l = 999999
        ans = ""

        while r < len(s):
            # print(l, r, window, form)
            curr = s[r]
            window[curr] += 1

            if curr in d_t and window[curr] == d_t[curr]:
                form += 1

            while l <= r and form == required:
                curr = s[l]

                if min_l > r-l+1:
                    min_l = r-l + 1
                    ans = s[l:r+1]
                
                window[curr] -= 1
                
                if curr in d_t and window[curr] < d_t[curr]:
                    form -= 1
                
                l += 1
            
            r += 1

        return ans


        
