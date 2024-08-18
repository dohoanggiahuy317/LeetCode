class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:

        dp1 = {}
        
        for i in range(len(s)):
            x, y = points[i]
            c = s[i]
            
            sq = max(abs(x), abs(y))
            
            if sq not in dp1:
                dp1[sq] = c
            else:
                dp1[sq] += c
        
        dp = []
        for u, v in dp1.items():
            dp.append([u, v])
            
        dp.sort(key = lambda x: x[0])
        
        
        ans = 0
        visited = set()
        
        met = False
        
        for s, c in dp:
            for charac in list(c):
                if charac in visited:
                    met = True
                    break
                visited.add(charac)
                
            if met:
                break
            #print(visited)
            ans += len(c)

            
        return ans
            
            
            
            
            
                    
        
        
        
        
        
                
        