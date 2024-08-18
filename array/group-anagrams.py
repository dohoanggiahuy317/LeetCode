class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for x in strs:
            t = "".join(sorted(list(x)))
            if t in d:
               d[t].append(x)
            else:
                d[t] = [x]
        
        return list(d.values())