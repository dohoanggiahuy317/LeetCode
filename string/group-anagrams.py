class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = [[strs[0]]]
        
        
        #loop qua cac string con lai
        for s in strs[1:]:
            got_anagram = False
            for group in groups:
                if Counter(s) == Counter(group[0]):
                    group.append(s)
                    got_anagram = True
            
            if not got_anagram:
                groups.append([s])
                
        return groups
        
        
        