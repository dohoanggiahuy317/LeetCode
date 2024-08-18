class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        
        while len(nums) > 0:
            x = nums.pop(0)
            y = nums.pop(0)
            arr.append(y)
            arr.append(x)
            
        return arr