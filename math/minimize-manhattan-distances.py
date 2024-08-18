class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        
        
        points.sort(key = lambda x: sum(x))
        points_pos = list(map(sum, points))
        d_pos = {}
        for x in range(len(points)):
            d_pos[x] = points_pos[x]
        
        
        d_neg = {}
        for i in range(len(points)):
            d_neg[i] = points[i][0] - points[i][1]
        points_neg = []
        for u, v in d_neg.items():
            points_neg.append([u, v]) 
        points_neg.sort(key = lambda x: x[1])
        
        ans = 10 ** 20

        for i in range(len(points)):
            s, l = 0, len(points) - 1
            
            if points_neg[s][0] == i:
                s += 1
            if points_neg[l][0] == i:
                l -= 1
                
            neg_diff = abs( points_neg[l][1] - points_neg[s][1] )
            pos_diff = abs( d_pos[ points_neg[l][0] ] - d_pos[ points_neg[s][0] ] )

            ans1 = max(neg_diff, pos_diff)


            s, l = 0, len(points) - 1

            if i == s:
                s += 1
            if i == l:
                l -= 1

            pos_diff = abs( points_pos[l] - points_pos[s] )
            neg_diff = abs( d_neg[l] - d_neg[s] )

            ans2 = max(pos_diff, neg_diff)

            fans = max(ans1, ans2)

            ans = min(ans, fans)

        return ans
        
        