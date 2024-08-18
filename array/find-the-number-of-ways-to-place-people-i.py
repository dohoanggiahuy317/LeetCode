class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        
        ans = 0
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                chi_x, chi_y = points[i]
                tak_x, tak_y = points[j]
                
                if chi_x <= tak_x and chi_y >= tak_y:
                    
                    b = True
    
                    for k in range(len(points)):
                        if k != i and k != j:
                            k_x, k_y = points[k]
                            if min(chi_x, tak_x) <= k_x <= max(chi_x, tak_x) and min(tak_y, chi_y) <= k_y <= max(tak_y, chi_y):
                                b = False
                                break

                    if b:
                        ans += 1                 
                    
        return ans