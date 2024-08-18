class Solution:
    def maximumLength(self, s: str) -> int:
        d = {}
        i = 0


        while i < len(s):
            curr = s[i]
            while i < len(s) - 1 and s[i] == s[i + 1]:
                i += 1
                curr += s[i]
                
            if curr[0] not in d:
                d[curr[0]] = {}
            
            if len(curr) not in d[curr[0]]:
                d[curr[0]][len(curr)] = 1
            else:
                d[curr[0]][len(curr)] += 1

            # for j in range(1, len(curr) + 1):
            #     if j not in d[curr[0]]:
            #         d[curr[0]][j] = 1
            #     else:
            #         d[curr[0]][j] += 1
                
            i += 1

        # print(d)
        ans = -1
        for char, appr in d.items():
            temp = {}
            for l, freq in appr.items():
                
                for k in range(1, l+1):
                    if k not in temp:
                        temp[k] = (l+1-k) * freq
                    else:
                        temp[k] += (l+1-k) * freq
                        
            for m, n in temp.items():
                if n >= 3:
                    ans = max(ans, m)
                
        
        return ans
        