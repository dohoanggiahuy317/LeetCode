class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        
        
        def dis(a, b):
            na = min(a, b)
            nb = max(a, b)
                        
            return min(ord(nb) - ord(na), ord("z") - ord(nb) + ord(na) - ord("a") + 1 )
        
        def sumdis(s, t):
            ans = 0
            for i in range(len(s)):
                ans += dis(s[i], t[i])
                
            return ans
        
        
        ans = ""
        
        
        for c in range(len(s)):
            if k <= 0:
                break
            
            i = ord("a")
            
            while dis(s[c], chr(i)) > k:
                i += 1
            
            k -= dis(s[c], chr(i))
            ans += chr(i)
            
            
        temp = len(ans)
        for i in range(temp, len(s)):
            ans += s[i]
           
        # print(ans)
        return ans
            
            