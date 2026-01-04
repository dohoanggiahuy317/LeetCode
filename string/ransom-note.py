class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_li = list(magazine)
        
        for i in ransomNote:
            if i in mag_li:
                mag_li.remove(i)
            else:
                return False
            
        return True
        