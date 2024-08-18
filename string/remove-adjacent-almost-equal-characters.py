class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        ans = 0
        l = 0
        
        for i in range(1, len(word)):
            if abs(ord(word[i]) - ord(word[i-1])) <= 1:
                continue
            else:
                ans += (i-l)//2
                l = i
                
        ans +=  (len(word)-l)//2
                
        return ans