class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        ans = 0
        
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                d = {}
                for x in s[i:j]:
                    if x in d:
                        d[x] += 1
                        
                    else:
                        d[x] = 1
                    
                valid = True
                for m, n in d.items():
                    if n > 2:
                        valid = False
                        break
                # print(s[i:j])
                if valid:
                
                    ans = max(ans, len(s[i:j]))
                    
                    
        return ans