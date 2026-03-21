class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        
        acronym = ""
        for word in words:
            acronym += word[0]
        
        
        if s == acronym:
            return True
        return False