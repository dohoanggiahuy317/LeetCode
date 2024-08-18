class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ta = []
        tb = -1
        
        ans = set()
        
          
        i = 0
        
        while i < len(s):
            
            if len(ta) > 0 and i - k > ta[0]:
                ta.pop(0)
            
            if i + len(b) <= len(s):
                if s[i:i + len(b)] == b:
                    for x in ta:
                        ans.add(x)
                    ta = []
                    tb = i
                        
            if i + len(a) <= len(s):
                 if s[i:i + len(a)] == a:
                    if tb >= 0 and i - tb <= k:
                        # ans[i] = 0
                        ans.add(i)
                    ta.append(i)
                        
            i += 1

                    
        # print(ans)
        return sorted(list(ans))
        # return sorted(list(ans.keys()))