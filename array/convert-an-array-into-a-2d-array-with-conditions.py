class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()    
        
        freq = Counter(nums)
        max_freq = max(freq.values())
        ans = [[] for _ in range(max_freq)]
        
        for x, f in freq.items():
            count = 0
            while start < f:
                ans[count].append(x)
                count += 1
        
        return ans
        