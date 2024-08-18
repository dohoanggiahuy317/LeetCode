class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for i in range(len(nums)):
            x = nums[i]
            if x not in d:
                d[x] = i
            else:
                if i - d[x] <= k:
                    return True
                d[x] = i
        
        return False
                
