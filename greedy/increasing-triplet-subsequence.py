class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False
            
        min_x = 0 # maintain the index min_x that has minimum value
        min_y = -1
        for i in range(1, len(nums)):
            if min_y == -1: # if min_y does not exist then try to create it
                if nums[min_x] < nums[i]: # we found a candidate for a[x] < a[y]
                    min_y = i
                else:
                    min_x = i # minimize min_x otherwise
            else:
                if nums[min_y] < nums[i]: # This is a solution
                    return True
                else: 
                    if nums[min_x] < nums[i]: # not a solution, but let's try to minimize min_y
                        min_y = i
                    else:
                        min_x = i # cannot minimize min_y, at least update min_x
        return False