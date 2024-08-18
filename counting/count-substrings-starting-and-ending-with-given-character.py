class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        ans = 0
        count = 0
        
        for i in range(len(s)):
            if s[i] == c:
                count += 1
        
            
                
        return count * (count - 1) // 2 + count