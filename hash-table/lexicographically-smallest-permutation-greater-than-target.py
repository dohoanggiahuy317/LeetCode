class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        
        perm = list()

        sList = SortedList(key = lambda x: -x)
        sList.update(map(ord, s))
        target = list(map(ord, target))
 
        for i, tChr in enumerate(target):
            if tChr in sList:
                sList.remove(tChr)
               
                if sList <= target[i+1:]:
                    sList.add(tChr)
                else: 
                    perm.append(tChr)
                    continue   
                    
            for sChr in reversed(sList):
                if sChr <= tChr: continue

                sList.remove(sChr)
                perm.append(sChr)
                perm.extend(sList[::-1])
                break

            return ''.join(map(chr, perm))
            
        return ''