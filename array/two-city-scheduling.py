class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n2 = len(costs)
        ans = sum(list(map(lambda x: x[0], costs)))

        diff = list(map(lambda x: x[1] - x[0], costs))
        diff.sort()

        ans += sum(diff[:int(n2/2)])
        
        return ans

        

        