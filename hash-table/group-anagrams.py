from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            k = tuple(sorted(list(s)))
            d[k].append(s)

        return list(d.values())
