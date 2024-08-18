class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        
        d = set()
        
        for i in range(len(s) - 1):
            d.add(s[i:i+2])
            
        for i in range(len(s) - 1):
            if s[i+1] + s[i] in d:
                return True
            
        return False