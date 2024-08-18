class Solution:
    def maximumLength(self, s: str) -> int:
        d = {}
        
        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                temp = s[i:j]
                if temp in d:
                    d[temp] += 1
                else:
                    d[temp] = 1
                    
                
        ans = -1
        for u, v in d.items():
            # print(u, v)
            if v >= 3 and len(set(list(u))) == 1:
                ans = max(ans, len(u))
                
             
        return ans