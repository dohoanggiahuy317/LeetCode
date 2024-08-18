class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        d = {}
        
        for u, v in pick:
            if u not in d:
                d[u] = {}
            if v not in d[u]:
                d[u][v] = 0
                
            d[u][v] += 1
            
        ans = 0
        # print(d)
        for k, v in d.items():
            for ball, num in d[k].items():
                if num > k:
                    ans += 1
                    break
                    
        return ans