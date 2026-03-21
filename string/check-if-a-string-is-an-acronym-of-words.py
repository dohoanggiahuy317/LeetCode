class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        
        arr = []
        for word in words:
            arr.append(word[0])
        
        if s == ''.join(arr):
            return True    
        return False