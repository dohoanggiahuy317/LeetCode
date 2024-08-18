class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        curr = {}
        diff = {}
        
        ans = []
        
        for b, c in queries:
            if b not in curr:
                curr[b] = c
            else:
                old_c = curr[b]
                if diff[old_c] == 1:
                    del diff[old_c]
                else:
                    diff[old_c] -= 1
                curr[b] = c
                    
            if c not in diff:
                diff[c] = 1
            else:
                diff[c] += 1
            ans.append(len(diff))
            # print(diff, curr)
            
        return ans
                
                
                