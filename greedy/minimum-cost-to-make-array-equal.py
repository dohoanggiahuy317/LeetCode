class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        nums_cost = list(zip(nums, cost))
        nums_cost.sort()
        
        iter_list = []
        for n, c in nums_cost:
            for _ in range(c):
                iter_list.append(n)
                
        median = iter_list[len(iter_list)//2]
        ans = sum(abs(median - num) * cost for num, cost in nums_cost)
        
        return ans