from functools import lru_cache
from typing import List

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        @lru_cache(None)
        def dp(index, last1, last2):
            if index == n:
                return 1 
            
            count = 0
            for value in range(last1, nums[index] + 1):
                arr1_value = value
                arr2_value = nums[index] - arr1_value
                
                if arr2_value <= last2:
                    count = (count + dp(index + 1, arr1_value, arr2_value)) % MOD
            
            return count
        
        return dp(0, 0, nums[0])