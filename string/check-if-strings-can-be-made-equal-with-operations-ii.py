class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        def split_str(s):
            sc = []
            sl = []
            
            for i in range(len(s)):
                if i % 2 == 0:
                    sc.append(s[i])
                else:
                    sl.append(s[i])
                    
            return sorted(sc), sorted(sl)
        
        sc1, sl1 = split_str(s1)
        sc2, sl2 = split_str(s2)
        
        # print(sc1, sl1)
        # print(sc2, sl2)
        
        return (sc1 == sc2 and sl1 == sl2)