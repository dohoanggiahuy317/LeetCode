import heapq

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        v1 = []
        v2 = []

        for i in range(len(values)):
            v1.append(values[i] - i)
            v2.append(values[i] + i)
        
        l = 0
        ans = 0

        for r in range(1, len(v1)):
            if v2[r-1] > v2[l]:
                l = r-1
            ans = max(ans, v1[r] + v2[l])
        
        return ans

        
